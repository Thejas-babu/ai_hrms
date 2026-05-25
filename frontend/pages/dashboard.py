import streamlit as st
import pandas as pd
import plotly.express as px

from backend.database.db import (
    conn,
    cursor
)

def show_dashboard():

    st.header("📊 Dashboard")

    # REAL EMPLOYEE COUNT

    cursor.execute(
        "SELECT COUNT(*) FROM employees"
    )

    employee_count = cursor.fetchone()[0]

    # REAL ATTENDANCE COUNT

    cursor.execute(
        "SELECT COUNT(*) FROM attendance"
    )

    attendance_count = cursor.fetchone()[0]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Employees",
        employee_count
    )

    col2.metric(
        "Attendance Marked",
        attendance_count
    )

    col3.metric(
        "AI Hiring Score",
        "89%"
    )

    # Department Analytics

    cursor.execute(
        '''
        SELECT department, COUNT(*)
        FROM employees
        GROUP BY department
        '''
    )

    data = cursor.fetchall()

    if data:

        df = pd.DataFrame(
            data,
            columns=[
                "Department",
                "Employees"
            ]
        )

        fig = px.bar(
            df,
            x="Department",
            y="Employees"
        )

        st.plotly_chart(fig)

    else:

        st.warning(
            "No employee data available"
        )
