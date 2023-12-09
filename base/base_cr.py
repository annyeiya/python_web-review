import sqlite3

db = sqlite3.connect('base.db')
cur = db.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS anime (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title text,
            year integer,
            genre text,
            links text,
            descriptions text,
            image text
            )''')

db.commit()
db.close()