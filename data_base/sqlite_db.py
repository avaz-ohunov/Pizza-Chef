# sqlite_db.py

import sqlite3 as sql
from reg_bot import bot

# Запуск БД
def sql_start():
	global base, cur
	base = sql.connect("pizza_chef.db")
	cur = base.cursor()
	base.execute("CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)")
	base.commit()


# Добавление данных в БД
async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute("INSERT INTO menu VALUES(?, ?, ?, ?)", tuple(data.values()))
		base.commit()


# чтение БД
async def sql_read(message):
	for ret in cur.execute("SELECT * FROM menu").fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f"{ret[1]}\n\nОписание: {ret[2]}\n\nЦена: ₽{ret[3]}")


# Чтение БД для админа
async def sql_read_admin():
	return cur.execute("SELECT * FROM menu").fetchall()


# Удаление данных из БД
async def sql_delete(data):
	cur.execute("DELETE FROM menu WHERE name == ?", (data,))
	base.commit()
