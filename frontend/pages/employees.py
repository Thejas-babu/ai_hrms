import streamlit as st
import random

from backend.database.db import (
    conn,
    cursor
)

def generate_employee_id():

    return f"EMP{random.randint(1000,9999)}"


def generate_pin():

    return str(random.randint(1000,9999))


def show_employees():

    st.header("👨‍💼 Employee Management")

    name = st.text_input(
        "Employee Name"
    )

    department = st.text_input(
        "Department"
    )

    if st.button("Add Employee"):

        employee_id = generate_employee_id()

        pin = generate_pin()

        try:

            cursor.execute(
                '''
                INSERT INTO employees
                (
                    employee_id,
                    name,
                    department,
                    pin
                )
                VALUES (?, ?, ?, ?)
                ''',
                (
                    employee_id,
                    name,
                    department,
                    pin
                )
            )

            conn.commit()

            st.success(
                "Employee Added Successfully ✅"
            )

            st.warning(
                "Save these credentials securely."
            )

            st.code(
                f'''
Employee ID: {employee_id}

PIN: {pin}
                '''
            )

        except:

            st.error(
                "Employee already exists"
            )
