import streamlit as st
from ai_modules.chatbot import ask_ai

def show_chatbot():

    st.header("🤖 AI HR Chatbot")

    question = st.text_input(
        "Ask HR Assistant"
    )

    if st.button("Ask"):

        answer = ask_ai(question)

        st.write(answer)
        