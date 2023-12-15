# скрипт для создания таблицы в базе данных, вызывается в build.sh
import sqlite3

with sqlite3.connect('base.db') as db:
    cur = db.cursor()
    cur.execute(''' CREATE TABLE IF NOT EXISTS anime (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                num integer,
                title text,
                year integer,
                genre text,
                links text,
                descriptions text,
                image text
                )''')

    db.commit()
