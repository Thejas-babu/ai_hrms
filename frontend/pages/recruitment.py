import streamlit as st
import pdfplumber

from ai_modules.resume_screening import score_resume

def extract_text_from_pdf(uploaded_file):

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

    return text


def show_recruitment():

    st.header("📄 AI Recruitment")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    job_description = st.text_area(
        "Job Description"
    )

    if uploaded_file and job_description:

        resume_text = extract_text_from_pdf(
            uploaded_file
        )

        score = score_resume(
            resume_text,
            job_description
        )

        st.success(
            f"AI Match Score: {score}%"
        )
