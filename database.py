import sqlite3

def init_db():
    conn = sqlite3.connect('dating.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        gender TEXT,
        age INTEGER,
        level INTEGER DEFAULT 1,
        hearts INTEGER DEFAULT 0
    )''')
    
    conn.commit()
    conn.close()
