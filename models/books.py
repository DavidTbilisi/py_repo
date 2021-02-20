import sqlite3
from db import db
from sqlalchemy import inspect

def object_as_dict(obj):
    if obj is not None:
        return {c.key: getattr(obj, c.key)
                for c in inspect(obj).mapper.column_attrs}
    return None

class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    author = db.Column(db.String(30))
    genre = db.Column(db.String(25))
    publishdate = db.Column(db.String(7))
    quantity = db.Column(db.Integer)


    @classmethod
    def find_by_name(cls, name):
        book = cls.query.filtery_by(name=name).first()
        return object_as_dict(book)

    @classmethod
    def find_by_id(cls, item_id):
        book = cls.query.filter_by(id=item_id).first()
        return object_as_dict(book)

    # TODO: update
    @classmethod
    def save(cls, item):
        cls.query.session.add(cls(**item))
        db.session.commit()

    @classmethod
    def delete(cls, item_id):
        to_del = cls.query.filter_by(id=item_id).first()
        db.session.delete(to_del)
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
