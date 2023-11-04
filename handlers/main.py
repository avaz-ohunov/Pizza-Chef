# main.py

from aiogram import types, Dispatcher
from reg_bot import dp 

# Основной режим бота
async def echo_message(message: types.Message):
	await message.answer("Такой команды нет")

# Обработчик других сообщений
def register_handlers_main(dp: Dispatcher):
	dp.register_message_handler(echo_message)
