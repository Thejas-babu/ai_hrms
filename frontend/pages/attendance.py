import streamlit as st
from datetime import datetime

from backend.database.db import (
    get_connection
)

def show_attendance():

    st.header("📅 Attendance System")

    employee_id = st.text_input(
        "Employee ID"
    )

    pin = st.text_input(
        "PIN",
        type="password"
    )

    action = st.selectbox(
        "Select Action",
        [
            "Check In",
            "Check Out"
        ]
    )

    if st.button("Submit"):

        conn = get_connection()

        cursor = conn.cursor()

        # Verify Employee

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

            current_time = datetime.now().strftime(
                "%H:%M:%S"
            )

            # Check Existing Record

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

            attendance = cursor.fetchone()

            # CHECK IN

            if action == "Check In":

                if attendance:

                    st.warning(
                        "Already checked in today ⚠️"
                    )

                else:

                    cursor.execute(
                        '''
                        INSERT INTO attendance
                        (
                            employee_id,
                            employee_name,
                            attendance_date,
                            check_in,
                            check_out
                        )
                        VALUES (?, ?, ?, ?, ?)
                        ''',
                        (
                            employee_id,
                            employee_name,
                            today,
                            current_time,
                            ""
                        )
                    )

                    conn.commit()

                    st.success(
                        f"Checked In at {current_time} ✅"
                    )

            # CHECK OUT

            elif action == "Check Out":

                if attendance:

                    if attendance[5]:

                        st.warning(
                            "Already checked out ⚠️"
                        )

                    else:

                        cursor.execute(
                            '''
                            UPDATE attendance
                            SET check_out=?
                            WHERE employee_id=?
                            AND attendance_date=?
                            ''',
                            (
                                current_time,
                                employee_id,
                                today
                            )
                        )

                        conn.commit()

                        st.success(
                            f"Checked Out at {current_time} ✅"
                        )

                else:

                    st.error(
                        "Please Check In first ❌"
                    )

        else:

            st.error(
                "Invalid Employee ID or PIN ❌"
            )

        conn.close()
