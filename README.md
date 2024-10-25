# How to Build with Groq

Welcome to the workshop on 'How to Build with Groq'. This repository contains several example scripts that demonstrate different ways to use the Groq API. Below, you'll find a guide to get started and an overview of each of the example files provided.

## Getting Started

To get started with the examples in this repository, you'll need to have the following prerequisites:

1. **Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Pip**: Ensure you have pip installed for managing Python packages.
3. **Groq API Key**: Sign up for a Groq account and obtain your API key.

### Installation

1. Clone this repository to your local machine:

   ```sh
   git clone https://github.com/yourusername/groq-workshop.git
   cd groq-workshop
   ```

2. Create a virtual environment (macos/linux):
   ```sh
   python3 -m venv env
   source env/bin/activate
   ```
3. Create a virtual environment (windows):

   ```sh
   python -m venv env
   env/Scripts/activate
   ```

4. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory of the repository and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Overview of Example Files

### chat.py

The `chat.py` script demonstrates how to use the Groq API to build a chatbot.

### audio.py

The `audio.py` script demonstrates how to use the Groq API to transcribe an audio file.

### team.py

The `team.py` script demonstrates how to use the Groq API to build a collaborative AI team. Each team member performs a specific duty, and the output of one member is passed to the next.

Key functions:

- `instruction_builder(duty, previous=None)`: Constructs the instruction prompt for each team member.
- `chat(prompt)`: Sends a chat request to the Groq API and returns the response.
- `team_chat(duty, previous=None)`: Manages the workflow of the AI team, passing outputs between members.

Example usage:
