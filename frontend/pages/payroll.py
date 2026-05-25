import streamlit as st
from reportlab.pdfgen import canvas

def generate_payslip(
    employee,
    salary
):

    filename = f"{employee}_payslip.pdf"

    c = canvas.Canvas(filename)

    c.drawString(
        100,
        750,
        f"Payslip for {employee}"
    )

    c.drawString(
        100,
        700,
        f"Salary: ₹{salary}"
    )

    c.save()

    return filename


def show_payroll():

    st.header("💰 Payroll")

    employee = st.text_input(
        "Employee Name"
    )

    salary = st.number_input(
        "Salary"
    )

    if st.button("Generate Payslip"):

        filename = generate_payslip(
            employee,
            salary
        )

        with open(filename, "rb") as file:

            st.download_button(
                label="Download Payslip",
                data=file,
                file_name=filename,
                mime="application/pdf"
            )
