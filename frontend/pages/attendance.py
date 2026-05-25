import streamlit as st

def show_attendance():

    st.header("📅 Attendance")

    employee = st.text_input("Employee Name")

    if st.button("Clock In"):
        st.success(f"{employee} clocked in")
        