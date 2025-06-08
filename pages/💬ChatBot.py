import streamlit as st
from openai import OpenAI

# Initialize OpenAI client (make sure your OPENAI_API_KEY is in .env or Streamlit secrets)
client = OpenAI()

st.title("💬 Virtual Assistant Chatbot")

# System prompt: define assistant's personality and purpose
system_prompt = """
You are a helpful assistant named 'App GuideBot' for a content creation and lead analysis platform.
Your job is to help users navigate the app and explain features such as:
1. Blog, caption, or video script generation
2. Viewing user profile
3. Checking blog SEO score
4. Predicting lead conversion from form or CSV
5. Exploring subscription plans and billing
6. Getting started with the chatbot

Answer like a friendly guide and keep your responses short and easy to understand.
"""

# Initialize chat history in session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": "Hi! 👋 I’m your assistant. Ask me anything about the app!"}
    ]

# Show chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box for user
user_prompt = st.chat_input("Ask about how to use the app...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages,
                temperature=0.7,
                max_tokens=300
            )
            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.chat_message("assistant").markdown(reply)
        except Exception as e:
            st.error(f"OpenAI error: {e}")
