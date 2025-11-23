from messages import Messages
from sentiment import sentimentanalyze
from wrapper import bot_prompt

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
    
    print("\n\nConversation Ended")

if __name__ == "__main__":
    main()