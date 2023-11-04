# reg_bot.py

from aiogram import Bot
from aiogram.dispatcher import Dispatcher 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from BotToken import bot_token

storage = MemoryStorage()

# Регистрация бота
bot = Bot(token = bot_token)
dp = Dispatcher(bot, storage = storage)
