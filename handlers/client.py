# client.py

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from reg_bot import dp, bot 
from keyboards import client_kb
from data_base import sqlite_db

# Обработка команд "start", "help"
async def start(message: types.Message):
	await message.answer("Приятного аппетита!", reply_markup = client_kb.buttons)


# Обработка команды "Режим_работы"
async def work_time(message: types.Message):
	await message.answer("Вс-Чт с 9:00 до 20:00,\nПт-Сб с 10:00 до 23:00")


# Обработка команды "Расположение"
async def location(message: types.Message):
	await message.answer("Ул. Колбасная, 15")


# Обработка команды "Меню"
async def menu(message: types.Message):
	await sqlite_db.sql_read(message)


# Обработчик команд клиента
def register_handlers_client(dp: Dispatcher):
	dp.register_message_handler(start, commands = ["start", "help", "client"])
	dp.register_message_handler(work_time, Text("Режим работы🕘", ignore_case = True))
	dp.register_message_handler(location, Text("Расположение📍", ignore_case = True))
	dp.register_message_handler(menu, Text("Меню📕", ignore_case = True))
