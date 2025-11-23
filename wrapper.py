import requests
import json
import os

api_key = os.getenv("OPENROUTER_API_KEY")

def bot_prompt(history):

    response = requests.post(
        url = "https://openrouter.ai/api/v1/chat/completions",
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "LiaPlus Assignment Chatbot"
        },

        json = {
            "model": "x-ai/grok-4.1-fast:free",
            "messages":history
        }
    )

    final = response.json()
    return final["choices"][0]["message"]["content"]