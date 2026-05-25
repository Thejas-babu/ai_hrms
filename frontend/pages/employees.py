import streamlit as st
from backend.database.db import conn, cursor

def show_employees():

    st.header("👨‍💼 Employee Management")

    name = st.text_input(
        "Employee Name"
    )

    department = st.text_input(
        "Department"
    )

    if st.button("Add Employee"):

        cursor.execute(
            '''
            INSERT INTO employees
            (name, department)
            VALUES (?, ?)
            ''',
            (name, department)
        )

        conn.commit()

        st.success(
            f"{name} added successfully"
        )

    st.subheader("Employee List")

    cursor.execute(
        "SELECT * FROM employees"
    )

    employees = cursor.fetchall()

    for emp in employees:

        st.write(
            f"ID: {emp[0]} | Name: {emp[1]} | Department: {emp[2]}"
        )
