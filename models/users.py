from db import db
from sqlalchemy import inspect


def object_as_dict(obj):
    if obj is not None:
        return {c.key: getattr(obj, c.key)
                for c in inspect(obj).mapper.column_attrs}
    return None


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {"username": self.username, "password": self.password}

    @classmethod
    def find_by_username(cls, username):
        user = User.query.filter_by(username=username).first()
        return user

    @classmethod
    def find_by_id(cls, id):
        user = User.query.filter_by(id=id).first()
        return user.json()

    def save(self):
        db.session.add(self)
        db.session.commit()
