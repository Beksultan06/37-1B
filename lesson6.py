

import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        age INTEGER,
        is_active BOOLEAN DEFAULT 1        
    )
""")

# CRUD 

# INSERT 

# cursor.execute("""
#     INSERT INTO users (username, email, age)
#     VALUES (?, ?, ?)
# """, ("bob", "bob123@gmail.com", 19))

# SELECT 
cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
# user = cursor.fetchall()
# print(user)
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

for user in users:
    print(user)

cursor.execute("""
    UPDATE users 
    SET username = ?
    WHERE id = ? 
""", ("admin", 1))

cursor.execute("DELETE FROM users WHERE id = ? ", (1,))

conn.commit()
conn.close()



