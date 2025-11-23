class Messages:
    def __init__(self):
        self.messages = []

    def usermessage(self, text, sentiment):
        merged = f"{text} (sentiment: {sentiment})"
        self.messages.append(
            {
                "role":"user",
                "content":merged
            }
        )
    
    def botmessage(self, text):
        self.messages.append(
            {
                "role":"assistant",
                "content":text
            }
        )
    
    def sendtomodel(self):
        return self.messages