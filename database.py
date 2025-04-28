import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def setup():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        gender TEXT,
        age INTEGER,
        premium INTEGER DEFAULT 0,
        registered_at TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS active_chats (
        chat_id INTEGER PRIMARY KEY,
        user1_id INTEGER,
        user2_id INTEGER,
        started_at TEXT,
        FOREIGN KEY (user1_id) REFERENCES users(user_id),
        FOREIGN KEY (user2_id) REFERENCES users(user_id)
    )
    ''')
    conn.commit()

def add_user(user_id, name, gender, age):
    cursor.execute('''
    INSERT OR REPLACE INTO users (user_id, name, gender, age, registered_at)
    VALUES (?, ?, ?, ?, ?)
    ''', (user_id, name, gender, age, datetime.now().isoformat()))
    conn.commit()

def get_user(user_id):
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    return cursor.fetchone()

def create_chat(user1_id, user2_id):
    cursor.execute('''
    INSERT INTO active_chats (user1_id, user2_id, started_at)
    VALUES (?, ?, ?)
    ''', (user1_id, user2_id, datetime.now().isoformat()))
    conn.commit()

def get_chat_by_user(user_id):
    cursor.execute('''
    SELECT * FROM active_chats WHERE user1_id = ? OR user2_id = ?
    ''', (user_id, user_id))
    return cursor.fetchone()

def delete_chat(chat_id):
    cursor.execute('DELETE FROM active_chats WHERE chat_id = ?', (chat_id,))
    conn.commit()
