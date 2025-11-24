def backup_chatbot(inputmsg):
    msg = inputmsg.lower()

    greetings = ["hello", "hi", "hey", "good morning", "good evening", "good afternoon"]
    negative = ["sad", "lonely", "miss", "confused","bad", "terrible", "worst", "disappointed", "angry", "upset","horrible"]
    positive = ["thank", "awesome", "great", "love", "good","nice","satsified","happy"]
    inquiries = ["help", "issue", "problem", "support", "service", "delay", "refund"]
    confusion = ["dont understand", "confusing", "what is", "explain"]
    apology = ["sorry", "my mistake", "apologize", "oops"]
    urgency = ["urgent", "asap", "quick", "immediately", "right now"]
    account = ["account", "login", "password", "username", "signin", "sign in"]
    payment = ["payment", "billing", "charge", "charged", "transaction"]
    product = ["product", "item", "package", "order"]
    waiting = ["waiting", "delay", "late", "pending"]
    gratitude = ["appreciate", "grateful", "thanks a lot", "really helped"]
    complaint = ["complain", "complaint", "not happy", "unacceptable"]
    choice = ["which", "choose", "option", "decide"]
    end_chat = ["bye", "goodbye", "see you", "later"]


    for word in greetings:
        if word in msg:
            return "Hello! How can I assist you today?"
    
    for word in negative:
        if word in msg:
            return "I understand this must be frustrating. I’m here to help, what exactly happened?"

    for word in positive:
        if word in msg:
            return "That's great! I'm here if you need more assistance."

    for word in inquiries:
        if word in msg:
            return "I’d be happy to help! Please tell me more."

    for word in confusion:
        if word in msg:
            return "No worries, I can clarify that for you. What part feels unclear?"

    for word in apology:
        if word in msg:
            return "It's completely okay. Let’s move forward and sort this out."

    for word in urgency:
        if word in msg:
            return "I understand it's urgent. I’ll help you as quickly as possible."

    for word in account:
        if word in msg:
            return "Let’s sort out your account issue. Can you share more details?"

    for word in payment:
        if word in msg:
            return "I can definitely help with your payment or billing concern, what seems to be the issue?"

    for word in product:
        if word in msg:
            return "Got it! Could you specify which product you're referring to?"

    for word in waiting:
        if word in msg:
            return "Thank you for your patience. Let me look into it."

    for word in gratitude:
        if word in msg:
            return "You're welcome!"

    for word in complaint:
        if word in msg:
            return "I’m really sorry to hear that! I shall work on it."

    for word in choice:
        if word in msg:
            return "I can help you decide, what options are you considering?"

    for word in end_chat:
        if word in msg:
            return "Goodbye."

    return "Sorry, I don't understand. Can you provide a bit more detail so I can assist better?"