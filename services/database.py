import sqlite3 as sql

DB_NAME = "database/users.db"

def connect_db():
    return sql.connect(DB_NAME)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_user(username, email, hash_password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
    (username,email,hash_password)
    )

    conn.commit()
    conn.close()

def find_user_by_username(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()
    conn.close()

    return result

def find_user_by_email(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM users WHERE email = ?",
        (email,)
    )
    result = cursor.fetchone()
    conn.close()

    return result
