import sqlite3
from models.users import User

users_list = [
    User(1, "user1", "password1"),
    User(2, "user2", "password2"),
    User(3, "user3", "password3"),
]

print('users: ', users_list)

conn = sqlite3.connect("data.sqlite")
c = conn.cursor()

# print(list(users_list[0].__dict__().values()))
# print(users_list[0].list())
# quit()

users = [u.list() for u in users_list]
print('users: ', users)

c.execute("CREATE TABLE IF NOT EXISTS users (id integer  primary  key, username varchar, password varchar )")

c.executemany("INSERT INTO users values (?, ?, ?)", users)
conn.commit()
conn.close()
