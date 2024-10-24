import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

filename = os.path.dirname(__file__) + "/first_30_seconds.mp3"

def transcribe(filename):
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
            file=(filename, file.read()),
            language="en"
        )
    return transcription.text



response = transcribe(filename)
print(response)

