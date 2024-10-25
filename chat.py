import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


messages=[
    {"role": "system", "content": "you are a helpful assistant."},
    {"role": "user", "content": "what is the best city in texas"},
    {"role": "assistant", "content": "san antonio"},
    {"role": "user", "content": "what is the best city in texas"},
    {"role": "assistant", "content": "san antonio"},
    {"role": "user", "content": "what is the best city in texas"},
    {"role": "user", "content": prompt},
]


def chat(prompt, messges):
    chat_completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages = messages
    )
    return chat_completion.choices[0].message.content



prompt = input("You: ")
response = chat(prompt)
print(response)


# system
# user
# assistant
