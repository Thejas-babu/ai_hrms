import sqlite3

conn = sqlite3.connect(
    "hrms.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Employee Table

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        department TEXT,
        private_key TEXT
    )
    '''
)

# Attendance Table

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_name TEXT,
        status TEXT
    )
    '''
)

conn.commit()
