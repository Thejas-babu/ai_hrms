import streamlit as st
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_payslip(
    employee_name,
    employee_id,
    department,
    basic_salary
):

    filename = f"{employee_name}_payslip.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    # Company Header

    title = Paragraph(
        "<b>FWC AI Pvt Ltd</b>",
        styles['Title']
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    # Payslip Title

    payslip_title = Paragraph(
        "<b>Employee Payslip</b>",
        styles['Heading2']
    )

    elements.append(payslip_title)

    elements.append(
        Spacer(1, 20)
    )

    # Employee Details

    employee_data = [
        ["Employee Name", employee_name],
        ["Employee ID", employee_id],
        ["Department", department],
        [
            "Pay Date",
            datetime.now().strftime("%Y-%m-%d")
        ]
    ]

    employee_table = Table(
        employee_data,
        colWidths=[150, 250]
    )

    employee_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica')
        ])
    )

    elements.append(employee_table)

    elements.append(
        Spacer(1, 20)
    )

    # Salary Breakdown

    hra = basic_salary * 0.20
    bonus = basic_salary * 0.10

    tax = basic_salary * 0.05
    pf = basic_salary * 0.03

    gross_salary = (
        basic_salary
        + hra
        + bonus
    )

    deductions = tax + pf

    net_salary = gross_salary - deductions

    salary_data = [
        [
            "Earnings",
            "Amount (₹)"
        ],

        [
            "Basic Salary",
            f"{basic_salary:.2f}"
        ],

        [
            "HRA",
            f"{hra:.2f}"
        ],

        [
            "Bonus",
            f"{bonus:.2f}"
        ],

        [
            "Tax Deduction",
            f"-{tax:.2f}"
        ],

        [
            "PF Deduction",
            f"-{pf:.2f}"
        ],

        [
            "Net Salary",
            f"{net_salary:.2f}"
        ]
    ]

    salary_table = Table(
        salary_data,
        colWidths=[250, 150]
    )

    salary_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),

            ('GRID', (0,0), (-1,-1), 1, colors.black),

            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),

            ('BACKGROUND', (0,1), (-1,-1), colors.beige)
        ])
    )

    elements.append(salary_table)

    elements.append(
        Spacer(1, 30)
    )

    # Footer

    footer = Paragraph(
        "This is a system-generated payslip.",
        styles['Italic']
    )

    elements.append(footer)

    # Build PDF

    doc.build(elements)

    return filename


def show_payroll():

    st.header("💰 Payroll Management")

    employee_name = st.text_input(
        "Employee Name"
    )

    employee_id = st.text_input(
        "Employee ID"
    )

    department = st.text_input(
        "Department"
    )

    basic_salary = st.number_input(
        "Basic Salary",
        min_value=0.0
    )

    if st.button("Generate Payslip"):

        filename = generate_payslip(
            employee_name,
            employee_id,
            department,
            basic_salary
        )

        with open(filename, "rb") as file:

            st.download_button(
                label="📥 Download Payslip",
                data=file,
                file_name=filename,
                mime="application/pdf"
            )
