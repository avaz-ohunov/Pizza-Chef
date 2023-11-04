# client_kb.py

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

kb1 = KeyboardButton("Режим работы🕘")
kb2 = KeyboardButton("Расположение📍")
kb3 = KeyboardButton("Меню📕")

buttons = ReplyKeyboardMarkup(resize_keyboard = True)
buttons.row(kb1, kb2).add(kb3)
