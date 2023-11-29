import flask
from flask import Flask, Response, render_template
import sqlite3
from time import sleep

sleep(45)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def start():
    db = sqlite3.connect('/base/base.db')
    cur = db.cursor()
    cur.execute('SELECT id, title, image FROM anime')
    data = cur.fetchall()
    db.close()
    return render_template('main.html', data=data)
    
@app.route('/<int:id>', methods=['GET'])
def display_details(id):
    db = sqlite3.connect('/base/base.db')
    cur = db.cursor()
    cur.execute('''SELECT title, year, genre, links, descriptions, image
                 FROM anime WHERE id=?''', (id,))
    details = cur.fetchone()
    db.close()
    return render_template('details.html', details=details)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)