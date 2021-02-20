import sqlite3
from db import db
from sqlalchemy import inspect

def object_as_dict(obj):
    if obj is not None:
        return {c.key: getattr(obj, c.key)
                for c in inspect(obj).mapper.column_attrs}
    return None

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))

    def __init__(self, user, password):
        self.username = user
        self.password = password

    def __repr__(self):
        return self.username

    def __dict__(self):
        return {"id": self.id, "username": self.username, "password": self.password}

    def list(self):
        return [self.id, self.username, self.password]

    @classmethod
    def find_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        print(user)
        return object_as_dict(user)

    @classmethod
    def add(cls, user, password):
        db.session.add(cls(user, password))
        db.commit()

