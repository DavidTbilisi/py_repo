import sqlite3
from db import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))

    def __init__(self, id, user, password):
        self.id = id
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
        conn = sqlite3.connect("data.sqlite")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", [username])
        user = c.fetchone()
        conn.close()
        return cls(*user) if user else None

    @classmethod
    def find_by_user_id(cls, user_id):
        conn = sqlite3.connect("data.sqlite")
        c = conn.cursor()
        c.execute("select * from users where id = ?", [user_id])
        user = c.fetchone()
        conn.close()
        return cls(*user) if user else None

    @classmethod
    def add(cls, user, password):
        conn = sqlite3.connect("data.sqlite")
        c = conn.cursor()
        c.execute("SELECT id from users ORDER BY id DESC")
        last_id = c.fetchone()[0]
        c.execute("INSERT INTO users VALUES(?, ?, ?)", [last_id + 1, user, password])
        conn.commit()
        return True

    @classmethod
    def rm(cls, user_id):
        conn = sqlite3.connect("data.sqlite")
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE  id = ? ", [user_id])
        conn.commit()
        return True
