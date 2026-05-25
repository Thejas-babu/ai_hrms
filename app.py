import streamlit as st

st.set_page_config(
    page_title="NeuroHR AI",
    layout="wide"
)

st.title("🚀 NeuroHR AI")

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Dashboard",
        "Employees",
        "Recruitment",
        "Payroll",
        "Attendance",
        "AI Chatbot"
    ]
)

if page == "Dashboard":
    from frontend.pages.dashboard import show_dashboard
    show_dashboard()

elif page == "Employees":
    from frontend.pages.employees import show_employees
    show_employees()

elif page == "Recruitment":
    from frontend.pages.recruitment import show_recruitment
    show_recruitment()

elif page == "Payroll":
    from frontend.pages.payroll import show_payroll
    show_payroll()

elif page == "Attendance":
    from frontend.pages.attendance import show_attendance
    show_attendance()

elif page == "AI Chatbot":
    from frontend.pages.chatbot import show_chatbot
    show_chatbot()