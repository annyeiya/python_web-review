import sqlite3
from config import base_path

def add_anime(num, title, year, genre, links, descriptions, image):
    with sqlite3.connect(base_path) as db:
        cur = db.cursor()
        cur.execute('''INSERT INTO anime 
                    (num, title, year, genre, links, descriptions, image)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                    (num, title, year, genre, links, descriptions, image))

        db.commit()

def update_anime(title, year, genre, links, descriptions, image, id):
    with sqlite3.connect(base_path) as db:
        cur = db.cursor()
        cur.execute("SELECT MAX(id) FROM anime") 
        last_id = cur.fetchone()[0]
        cur.execute('''UPDATE anime SET 
                    title = ?,
                    year = ?,
                    genre = ?,
                    links = ?,
                    descriptions = ?,
                    image = ?
                    WHERE id = ?''', 
                    (title, year, genre, links, descriptions, image, last_id - id))
        
        db.commit()
