import streamlit as st
from messages import Messages
from summarize import summarize, overall_sentiment
from wrapper import bot_prompt
from sentiment import sentimentanalyze

st.title ("LiaPlus AI - AI Chatbot with Sentiment Analyis")
st.write("Note: Please use an openrouter api key to access LLM functionality. Refer to README for instructions.")

if "msgs" not in st.session_state:
    st.session_state.msgs = Messages()

if "chat" not in st.session_state:
    st.session_state.chat = []

st.write("T: Hello! My name is T, your virtual assistant!")
inp = st.text_input("Enter:","")

if st.button("Send"):
    if inp.strip():
        sentiment = sentimentanalyze(inp)
        st.session_state.msgs.usermessage(inp,sentiment)

        bot_reply = bot_prompt(st.session_state.msgs.sendtomodel())
        st.session_state.msgs.botmessage(bot_reply)

        st.session_state.chat.append(("You", inp))
        st.session_state.chat.append(("T", bot_reply))

for role, msg in st.session_state.chat:
    if role == "You":
        st.write(f"{role}: {msg}  (Sentiment: {sentimentanalyze(msg)})")
    else:
        st.write(f"{role}: {msg}")

if st.button("End Conversation"):
    ovr = overall_sentiment(st.session_state.msgs)
    st.write("Overall Sentiment: ",ovr)

    summary = summarize(st.session_state.msgs.sendtomodel())
    st.write ("Conversation Summary: \n")
    st.write(summary)

