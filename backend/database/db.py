import sqlite3

conn = sqlite3.connect(
    "hrms.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        department TEXT
    )
    '''
)

conn.commit()
