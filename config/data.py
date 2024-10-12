import sqlite3 as sq

db = sq.connect('data.db')
cur = db.cursor()

async def db_start():
    cur.execute("""CREATE TABLE IF NOT EXISTS users_data(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                username TEXT,
                age TEXT,
                auth TEXT,
                added_at DATETIME DEFAULT CURRENT_TIMESTAMP)""")

# user data
def new_user(user_id, name, username, age, auth):
    cur.execute("SELECT user_id FROM users_data WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO users_data (user_id, name, username, age, auth) VALUES (?, ?, ?, ?, ?)", (user_id, name, username, age, auth))
        db.commit()
        return True
    else:
        return False

def get_user(user_id):
    cur.execute("SELECT * FROM users_data WHERE user_id = ?", (user_id,))
    row = cur.fetchone()
    if row:
        return row
    else:
        return None

# def add_book()

# def new_book()