class Messages:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are T, a friendly and empathetic customer service chatbot. "
                    "Always refer to yourself as T, never as Grok or an AI model. "
                    "Your tone should be warm, supportive, and concise. "
                    "Do not mention that you are an AI. "
                    "Help the user with their issues, ask clarifying questions, "
                    "and keep the conversation natural."
                )
            }
        ]
        self.usersentiment = []

    def usermessage(self, text, sentiment):
        merged = f"{text} (sentiment: {sentiment})"
        self.messages.append(
            {
                "role":"user",
                "content":merged
            }
        )
        self.usersentiment.append(sentiment)
    
    def botmessage(self, text):
        self.messages.append(
            {
                "role":"assistant",
                "content":text
            }
        )
    
    def sendtomodel(self):
        return self.messages