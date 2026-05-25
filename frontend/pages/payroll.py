import streamlit as st

def show_payroll():

    st.header("💰 Payroll")

    employee = st.text_input("Employee Name")
    salary = st.number_input("Salary")

    if st.button("Generate Payslip"):
        st.success(
            f"Payslip generated for {employee}"
        )