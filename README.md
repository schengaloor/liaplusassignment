#LiaPlus AI - AI Engineer Intern Assignment
Chatbot with Sentiment Analysis

###1. Overview:
   - LLM-based chatbot
   - Sentiment analysis using transformers
   - Simple streamlit frontend
   - Conversation summarization
   - Backup offline chatbot in case of LLM unavailability

###2. How to setup and use

   A. Install all required packages using: `pip install -r requirements.txt`

   B. Obtain API Key for LLM Functionality
   - Create an API Key on `https://openrouter.ai/settings/keys` (doesn't matter what you name it).
   - Don't worry about credit limits, the model being used is free of charge.
   - After creating key, add to environment variables by opening Windows CMD as admin, and entering the line: `setx OPENROUTER_API_KEY "please_enter_api_key_here"`
   - Restart CMD, and enter `%OPENROUTER_API_KEY%`, you're all set if you see your API key.
  
   C. Run the chatbot
   - enter `streamlit run front.py` in terminal
   - OR
   - run `main.py` on terminal

###3. Technologies Used
   - Python 3.10.9
   - HuggingFace Transformers - [DistillBERT](https://huggingface.co/docs/transformers/en/model_doc/distilbert)
   - [Grok 4.1 Fast using openrouter API](https://openrouter.ai/x-ai/grok-4.1-fast:free)
   - [Streamlit](https://streamlit.io/)
