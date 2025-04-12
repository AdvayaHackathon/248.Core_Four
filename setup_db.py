import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
""")

# Sample teachers
teachers = [
    ("teacher1", "pass123"),
    ("teacher2", "abc123"),
    ("admin", "admin123"),
    ("math_teacher", "math456")
]

cursor.executemany("INSERT INTO teachers (username, password) VALUES (?, ?)", teachers)

conn.commit()
conn.close()
