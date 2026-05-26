import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def ask_ai(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content
