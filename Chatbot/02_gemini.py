from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

completion = client.chat.completions.create(
    model="gemini-3.5-flash-lite",
    messages=[
        {"role": "system", "content": "You are a person named Aditya. Please analyze chat history and respond like Aditya and continue to chat"},
        {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)