import streamlit as st

from backend.database.db import (
    conn,
    cursor
)

def show_attendance():

    st.header("📅 Attendance")

    employee_id = st.text_input(
        "Employee ID"
    )

    pin = st.text_input(
        "PIN",
        type="password"
    )

    if st.button("Mark Attendance"):

        cursor.execute(
            '''
            SELECT * FROM employees
            WHERE employee_id=? AND pin=?
            ''',
            (
                employee_id,
                pin
            )
        )

        employee = cursor.fetchone()

        if employee:

            employee_name = employee[2]

            cursor.execute(
                '''
                INSERT INTO attendance
                (
                    employee_id,
                    employee_name,
                    status
                )
                VALUES (?, ?, ?)
                ''',
                (
                    employee_id,
                    employee_name,
                    "Present"
                )
            )

            conn.commit()

            st.success(
                f"Attendance Marked for {employee_name} ✅"
            )

        else:

            st.error(
                "Invalid Employee ID or PIN ❌"
            )
