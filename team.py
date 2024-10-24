import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def instruction_builder(duty, previous=None):
    instruction_prompt = f"""
    Your job is to: {duty}
    """
    if previous:
        instruction_prompt += f"""
        \n\n
        Here is the previous members output: {previous}
        """
    return instruction_prompt

def chat(prompt):
    chat_completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
    )
    return chat_completion.choices[0].message.content

def team_chat(duty, previous=None):
    instruction = instruction_builder(duty, previous)
    response = chat(instruction)
    print(response)
    print("-------")
    return chat(instruction)

system_prompt = """
You are a member of an AI team.
You will be passed the output of the previous members output,
and you will perform your duty.
"""

story = team_chat("Write a story about a team of 4 who are attending a hackathon together.")
summary = team_chat("Summarize this story", story)
extended_story = team_chat("Expand on the original story, adding more details and character development", story)
story_outcome = team_chat("Write about how the story ends, including the results of the hackathon", extended_story)

