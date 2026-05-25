import streamlit as st
from datetime import datetime

from backend.database.db import (
    get_connection
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

        conn = get_connection()

        cursor = conn.cursor()

        # Check Employee

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

            today = datetime.now().strftime(
                "%Y-%m-%d"
            )

            # Check Existing Attendance

            cursor.execute(
                '''
                SELECT * FROM attendance
                WHERE employee_id=?
                AND attendance_date=?
                ''',
                (
                    employee_id,
                    today
                )
            )

            existing = cursor.fetchone()

            if existing:

                st.warning(
                    "Attendance already marked today ⚠️"
                )

            else:

                cursor.execute(
                    '''
                    INSERT INTO attendance
                    (
                        employee_id,
                        employee_name,
                        status,
                        attendance_date
                    )
                    VALUES (?, ?, ?, ?)
                    ''',
                    (
                        employee_id,
                        employee_name,
                        "Present",
                        today
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

        conn.close()
