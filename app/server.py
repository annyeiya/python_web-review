import flask
from flask import Flask, Response, render_template
import sqlite3
from time import sleep
from config import base_path

sleep(20)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def start():
    ''' начальная страница, 
    выводит названия и картинки всех аниме из базы '''
    with sqlite3.connect(base_path) as db:
        cur = db.cursor()
        cur.execute('''SELECT id, title, image FROM anime 
                    ORDER BY num DESC''')
        data = cur.fetchall()

    return render_template('main.html', data=data)
    
@app.route('/<int:id>', methods=['GET'])
def display_details(id):
    ''' страницы с подробной информацие о выбранном анимэ '''
    with sqlite3.connect(base_path) as db:
        cur = db.cursor()
        cur.execute('''SELECT title, year, genre, links, descriptions, image
                    FROM anime WHERE id=?''', (id,))
        details = cur.fetchone()

    return render_template('details.html', details=details)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
