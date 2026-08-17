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

'''def add_role_column():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        ALTER TABLE users
        ADD COLUMN role TEXT NOT NULL DEFAULT 'User'
    """)

    conn.commit()
    conn.close()'''

def insert_user(username, email, hash_password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO users (username, email, password, role) 
        VALUES (?, ?, ?, ?)
    """,
        (username,email,hash_password,"User")
    )

    conn.commit()
    conn.close()

def find_user_by_username(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username, email, password, role FROM users WHERE username = ?",
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

def find_other_user_by_username(username, user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE username = ? AND id != ?
        """,
        (username, user_id)
    )

    result = cursor.fetchone()
    conn.close()

    return result

def find_other_user_by_email(email, user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE email = ? AND id != ?
        """,
        (email, user_id)
    )

    result = cursor.fetchone()
    conn.close()

    return result

def update_user(user_id,username,email):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET username = ?, email = ?
        WHERE id = ?
    """, (username, email, user_id))

    conn.commit()
    conn.close()

def select_password(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """ 
        SELECT password
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    )
    result = cursor.fetchone()
    conn.close()

    return result

def update_password(user_id,password_hash):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET password = ?
        WHERE id = ?
    """, (password_hash,user_id))

    conn.commit()
    conn.close()

def update_role(user_id,new_role):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET role = ?
        WHERE id = ?
    """, (new_role,user_id))

    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM users
        WHERE id = ?
    """, (user_id,))

    conn.commit()
    conn.close()

def get_all_users():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, email, role
        FROM users
    """)

    users = cursor.fetchall()
    conn.close()

    return users
