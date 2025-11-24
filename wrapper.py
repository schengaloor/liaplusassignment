import requests
import json
import os
from backup import backup_chatbot

api_key = os.getenv("OPENROUTER_API_KEY")

def bot_prompt(history):
    if not api_key:
        return "(BACKUP!) " + backup_chatbot(history[-1]["content"])
    
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
    
    if "error" in final:
        return "(BACKUP!) " + backup_chatbot(history[-1]["content"])
    
    return final["choices"][0]["message"]["content"]
