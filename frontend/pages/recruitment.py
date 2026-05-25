import streamlit as st
from ai_modules.resume_screening import score_resume

def show_recruitment():

    st.header("📄 AI Recruitment")

    uploaded_file = st.file_uploader(
        "Upload Resume"
    )

    job_description = st.text_area(
        "Job Description"
    )

    if uploaded_file and job_description:

        resume_text = uploaded_file.read().decode()

        score = score_resume(
            resume_text,
            job_description
        )

        st.success(f"AI Match Score: {score}%")
        