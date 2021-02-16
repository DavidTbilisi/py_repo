import sqlite3
from db import db

class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    author = db.Column(db.String(30))
    genre = db.Column(db.String(25))
    publishdate = db.Column(db.String(7))
    quantity = db.Column(db.Integer)


    @classmethod
    def find_by_name(cls):
        pass

    @classmethod
    def greatest_id(cls):
        conn = sqlite3.connect("data.sqlite")
        c = conn.cursor()
        c.execute("select id from books order by id desc")
        ret = c.fetchone()
        conn.close()
        return ret[0]

    @classmethod
    def find_by_id(cls, item_id):
        conn = sqlite3.connect("data.sqlite")
        c = conn.cursor()
        c.execute("select * from books where id = ?", [item_id])
        ret = c.fetchone()
        conn.close()
        return ret

    @classmethod
    def insert(cls, item):
        conn = sqlite3.connect("data.sqlite")
        c = conn.cursor()
        vals = list(item.values())
        vals = [cls.greatest_id()+1] + vals
        c.execute("INSERT INTO books VALUES(?, ?, ?, ?, ?, ?)", vals)
        conn.commit()
        conn.close()

    @classmethod
    def update(cls, book, item_id):
        conn = sqlite3.connect("data.sqlite")
        c = conn.cursor()
        c.execute("UPDATE books SET  name = ?, author = ?, genre = ?, publishDate = ?, quantity = ? where id = ?",
                  [book['name'], book['author'], book['genre'], book['publishDate'], book['quantity'], item_id])
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, item_id):
        conn = sqlite3.connect("data.sqlite")
        c = conn.cursor()
        c.execute("DELETE FROM books WHERE id = ?", [item_id])
        conn.commit()
        conn.close()


class AllBooks:
    @classmethod
    def get(cls):
        conn = sqlite3.connect("data.sqlite")
        c = conn.cursor()
        c.execute("select * from books order by id asc")
        ret = c.fetchall()
        conn.close()
        return ret

    @classmethod
    def delete(cls):
        conn = sqlite3.connect("data.sqlite")
        c = conn.cursor()
        c.execute("DELETE FROM books WHERE id > ?", [0])
        conn.commit()
        conn.close()
        return "Okay"
