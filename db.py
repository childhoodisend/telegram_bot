import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER NOT NULL, username TEXT NOT NULL)")


def print_table():
    for row in cursor.execute("SELECT * FROM users"):
        print(row)


def insert_into_table(user_id: int, username: str):
    pair = [(user_id, username)]
    cursor.executemany("INSERT OR REPLACE INTO users VALUES (?, ?)", pair)
    conn.commit()

    print_table()
