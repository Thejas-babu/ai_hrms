import streamlit as st
import pandas as pd
import plotly.express as px

from backend.database.db import (
    get_connection
)

def show_dashboard():

    st.header("📊 Dashboard")

    conn = get_connection()

    cursor = conn.cursor()

    # Employee Count

    cursor.execute(
        "SELECT COUNT(*) FROM employees"
    )

    employee_count = cursor.fetchone()[0]

    # Attendance Count

    cursor.execute(
        "SELECT COUNT(*) FROM attendance"
    )

    attendance_count = cursor.fetchone()[0]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Employees",
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
        SELECT department,
        COUNT(*)
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

        fig = px.pie(
            df,
            names="Department",
            values="Employees"
        )

        st.plotly_chart(fig)

    conn.close()
