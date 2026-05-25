import streamlit as st
import uuid

from backend.database.db import (
    conn,
    cursor
)

def generate_private_key():

    return str(uuid.uuid4())[:8]


def show_employees():

    st.header("👨‍💼 Employee Management")

    name = st.text_input(
        "Employee Name"
    )

    department = st.text_input(
        "Department"
    )

    if st.button("Add Employee"):

        private_key = generate_private_key()

        try:

            cursor.execute(
                '''
                INSERT INTO employees
                (name, department, private_key)
                VALUES (?, ?, ?)
                ''',
                (
                    name,
                    department,
                    private_key
                )
            )

            conn.commit()

            st.success(
                f"Employee Added Successfully"
            )

            st.info(
                f"Private Key: {private_key}"
            )

        except:

            st.error(
                "Employee already exists"
            )
