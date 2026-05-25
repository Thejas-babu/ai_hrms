import sqlite3

conn = sqlite3.connect(
    "hrms.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Employees Table

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT UNIQUE,
        name TEXT,
        department TEXT,
        pin TEXT
    )
    '''
)

# Attendance Table

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT,
        employee_name TEXT,
        status TEXT
    )
    '''
)

conn.commit()
