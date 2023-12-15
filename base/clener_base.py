# скрипт для отчистки базы данных и обнуления числа запусков проекта 
import sqlite3

with sqlite3.connect('base.db') as db:
        cur = db.cursor()
        cur.execute('''DELETE FROM anime''')
        db.commit()

with open("run_num.txt", "w") as file:
    file.write(str(0))
