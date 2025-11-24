from wrapper import bot_prompt

def overall_sentiment(msgs):
    sents = msgs.usersentiment

    pos = sents.count("POSITIVE")
    neg = sents.count("NEGATIVE")

    if pos > neg:
        return "POSITIVE"
    elif neg > pos:
        return "NEGATIVE"
    else:
        return "NEUTRAL"

    

def backup_summary(history):
    usermsgs = []
    for m in history:
        if m["role"] == "user":
            usermsgs.append(m["content"])
    
    if not usermsgs:
        return "No input."

    first = usermsgs[0]
    last = usermsgs[-1]

    return (
        "Conversation Summary (Backup):\n"
        f"- The conversation started with: '{first}'\n"
        f"- The last message was: '{last}'\n"
        "- LLM unavailable, this is a backup offline rule-based summary."
    )

def summarize(history):

    summarize = [
        {
            "role": "system",
            "content": "You are a summarization model. Summarize this entire conversation in not more than 3 to 5 sentences. Focus on emotions, tone, critical points discussed, mood shifts, or any other key points that are worth mentioning."
        }
    ]

    complete_conversation = summarize + history
    summary = bot_prompt(complete_conversation)

    if summary.startswith("(BACKUP!) "):
        return backup_summary(history)

    return summary

