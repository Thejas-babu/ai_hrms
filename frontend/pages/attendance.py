import streamlit as st

from backend.database.db import (
    conn,
    cursor
)

def show_attendance():

    st.header("📅 Attendance")

    employee_name = st.text_input(
        "Employee Name"
    )

    private_key = st.text_input(
        "Private Key",
        type="password"
    )

    if st.button("Mark Attendance"):

        cursor.execute(
            '''
            SELECT * FROM employees
            WHERE name=? AND private_key=?
            ''',
            (
                employee_name,
                private_key
            )
        )

        employee = cursor.fetchone()

        if employee:

            cursor.execute(
                '''
                INSERT INTO attendance
                (employee_name, status)
                VALUES (?, ?)
                ''',
                (
                    employee_name,
                    "Present"
                )
            )

            conn.commit()

            st.success(
                "Attendance Marked Successfully ✅"
            )

        else:

            st.error(
                "Invalid Name or Private Key ❌"
            )
