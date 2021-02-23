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

    def __init__(self, name, author, genre, publishdate, quantity):
        self.name = name
        self.author = author
        self.genre = genre
        self.publishdate = publishdate
        self.quantity = quantity

    def json(self):
        if self != None:
            return {
                'name': self.name,
                'author': self.author,
                'genre': self.genre,
                'publishdate': self.publishdate,
                'quantity': self.quantity
            }
        return None

    @classmethod
    def find_by_name(cls, name):
        book = cls.query.filter_by(name=name).first()
        return book

    @classmethod
    def find_by_id(cls, item_id):
        book = cls.query.filter_by(id=item_id).first()
        return book

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


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
