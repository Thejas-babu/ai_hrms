from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("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")
)

def ask_ai(question):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content
