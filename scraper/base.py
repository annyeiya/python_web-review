import sqlite3

def add_anime(title, year, genre, links, descriptions, image):
    db = sqlite3.connect('/base/base.db')
    cur = db.cursor()
    cur.execute('''INSERT INTO anime 
                (title, year, genre, links, descriptions, image)
                VALUES (?, ?, ?, ?, ?, ?)''', 
                (title, year, genre, links, descriptions, image))
    
    db.commit()
    db.close()


def update_anime(title, year, genre, links, descriptions, image, id):
    db = sqlite3.connect('/base/base.db')
    cur = db.cursor()
    cur.execute('''UPDATE anime SET 
                title = ?,
                year = ?,
                genre = ?,
                links = ?,
                descriptions = ?,
                image = ?
                WHERE id = ?''', 
                (title, year, genre, links, descriptions, image, id))
    
    db.commit()
    db.close()
  