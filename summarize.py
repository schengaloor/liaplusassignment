from wrapper import bot_prompt

def summarize(history):

    
    summarize = [
        {
            "role": "system",
            "content": "You are a summarization model. Summarize this entire conversation in not more than 3 to 5 sentences. Focus on emotions, tone, critical points discussed, mood shifts, or any other key points that are worth mentioning."
        }
    ]

    complete_conversation = summarize + history
    summary = bot_prompt(complete_conversation)

    return summary