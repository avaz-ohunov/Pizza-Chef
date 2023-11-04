# admin_kb.py

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

kb1 = KeyboardButton("🟢 Добавить🍕")
kb2 = KeyboardButton("🔴 Удалить🍕")

buttons = ReplyKeyboardMarkup(resize_keyboard = True)
buttons.row(kb1, kb2)

button_cancel = ReplyKeyboardMarkup(resize_keyboard = True)
button_cancel.add("Отмена")
