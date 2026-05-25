import streamlit as st

def show_employees():

    st.header("👨‍💼 Employee Management")

    name = st.text_input("Employee Name")
    department = st.text_input("Department")

    if st.button("Add Employee"):
        st.success(f"{name} added successfully")