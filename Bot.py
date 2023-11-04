# Bot.py

from aiogram.utils import executor
from reg_bot import dp
from handlers import admin, client, main
from data_base import sqlite_db
from datetime import datetime

# Запуск бота
async def on_startup(_):
	time_now = datetime.today()
	sqlite_db.sql_start()
	print(f"[{str(time_now)[:19]}]: Бот успешно запущен")


# Регистрация обработчиков сообщений
admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
main.register_handlers_main(dp)


# Работа бота
executor.start_polling(dp, skip_updates = True, on_startup = on_startup)
