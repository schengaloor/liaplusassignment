from messages import Messages
from sentiment import sentimentanalyze
from wrapper import bot_prompt
from summarize import summarize, overall_sentiment

def main():
    print('T: Hello! My name is T! How may I help you?')

    msgs = Messages()

    while True:
        inp = str(input("Enter: "))

        if inp.lower() == "exit" or inp.lower() == "stop":
            break

        sentiment = sentimentanalyze(inp)
        print("Sentiment: ",sentiment)

        msgs.usermessage(inp,sentiment)

        bot_reply = bot_prompt(msgs.sendtomodel())

        print("T: ",bot_reply)
        print("\n")

        msgs.botmessage(bot_reply)
    
    print("\n\nConversation Ended\n\n")
    
    ovr = overall_sentiment(msgs)
    summary = summarize(msgs.sendtomodel())

    print("Overall Conversation Sentiment: ",ovr)
    print("\n")
    print("Summary of this conversation: \n",summary)


if __name__ == "__main__":
    main()