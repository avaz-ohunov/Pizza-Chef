# admin.py

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from reg_bot import dp, bot
from data_base import sqlite_db
from keyboards import admin_kb

# Класс состояний
class FSMAdmin(StatesGroup):
	photo = State()
	name = State()
	description = State()
	price = State()


# Проверка админа
async def verification(message: types.Message):
	if message.from_user.id == 1142268145:
		await message.answer("Панель администратора👇", reply_markup = admin_kb.buttons)


# Запуск состояния
async def cm_start(message: types.Message):
	if message.from_user.id == 1142268145:
		await FSMAdmin.photo.set()
		await message.answer("Загрузите фото📷", reply_markup = admin_kb.button_cancel)


# Отмена состояния
async def cancel_handler(message: types.Message, state: FSMContext):
	current_state = await state.get_state()
	
	if current_state is None:
		return None
	
	await state.finish()
	await message.answer("ОК", reply_markup = admin_kb.buttons)


# Грузим id фото в словарь
async def load_photo(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data["photo"] = message.photo[0].file_id

	await FSMAdmin.next()
	await message.answer("Теперь введите название")


# Получаем название пиццы
async def get_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data["name"] = message.text

	await FSMAdmin.next()
	await message.answer("Введите описание")


# Получаем описание пиццы
async def get_description(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data["description"] = message.text

	await FSMAdmin.next()
	await message.answer("Укажите цену")


# Получаем цену пиццы и завершаем состояние
async def get_price(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data["price"] = int(message.text)

	await sqlite_db.sql_add_command(state)
	await state.finish()
	await message.answer("В меню новая пицца🍕", reply_markup = admin_kb.buttons)


# Создаём inline-кнопку
@dp.callback_query_handler(lambda x: x.data and x.data.startswith("del "))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete(callback_query.data.replace("del ", ""))	
	await callback_query.answer("Пицца удалена из меню", show_alert = True)
	await bot.delete_message(chat_id = callback_query.from_user.id, message_id = callback_query.message.message_id)


# Метод удаления пиццы из меню
async def delete_pizza(message: types.Message):
	if message.from_user.id == 1142268145:
		data = await sqlite_db.sql_read_admin()
		for ret in data:
			await bot.send_photo(message.from_user.id, ret[0], f"{ret[1]}\n\nОписание: {ret[2]}\n\nЦена: ₽{ret[3]}",
					reply_markup = InlineKeyboardMarkup().add(InlineKeyboardButton("Удалить", callback_data = f"del {ret[1]}")))


# Обработчик команд админа
def register_handlers_admin(dp: Dispatcher):
	dp.register_message_handler(verification, commands = ["admin"])
	dp.register_message_handler(cm_start, Text("🟢 Добавить🍕", ignore_case = True), state = None)
	dp.register_message_handler(cancel_handler, Text("Отмена", ignore_case = True), state = "*")
	dp.register_message_handler(load_photo, content_types = ["photo"], state = FSMAdmin.photo)
	dp.register_message_handler(get_name, state = FSMAdmin.name)
	dp.register_message_handler(get_description, state = FSMAdmin.description)
	dp.register_message_handler(get_price, state = FSMAdmin.price)	
	dp.register_message_handler(delete_pizza, Text("🔴 Удалить🍕", ignore_case = True))
