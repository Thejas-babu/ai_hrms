import sqlite3

def get_connection():

    conn = sqlite3.connect(
        "hrms.db",
        check_same_thread=False
    )

    return conn


def init_db():

    conn = get_connection()

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
        attendance_date TEXT,
        check_in TEXT,
        check_out TEXT
    )
    '''
)

    conn.commit()

    conn.close()


init_db()
