import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard():

    st.header("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Employees", "500")
    col2.metric("Attendance", "92%")
    col3.metric("AI Hiring Score", "89%")

    df = pd.DataFrame({
        "Department": ["HR", "IT", "Sales"],
        "Employees": [20, 50, 30]
    })

    fig = px.bar(
        df,
        x="Department",
        y="Employees"
    )

    st.plotly_chart(fig)