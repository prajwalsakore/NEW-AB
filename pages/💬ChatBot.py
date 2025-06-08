import streamlit as st
from openai import OpenAI

# Initialize OpenAI client using Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Chatbot Assistant", page_icon="🤖")
st.title("🤖 AI Assistant Chatbot")
st.write("Ask me anything about using this app!")

# System prompt to give the chatbot context about your app structure
system_prompt = {
    "role": "system",
    "content": """
You are an AI assistant for an AI-powered content generation app. Your job is to help users navigate the app and provide friendly guidance.

Here is how the app is structured:

1. **Home Page** – Where users enter their username, email, and role (e.g., Student, Marketer, Content Creator).
2. **Generate** – Allows users to create blog posts, email content, and social media captions using AI.
3. **Content Ideas** – Suggests blog, email, or caption ideas based on user input.
4. **Plans and Billing** – Displays available subscription plans (Basic ₹0, Pro ₹199, Premium ₹499) and includes a dummy billing system.
5. **User Info** – Displays stored user data such as name, email, and selected plan.

If the user asks where to perform an action, always guide them by referring to the tab names above.
"""
}

# Initialize chat session state
if "messages" not in st.session_state:
    st.session_state.messages = [system_prompt]

# Display chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle new user input
prompt = st.chat_input("Ask your question...")
if prompt:
    # Add user's message to session
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call OpenAI ChatCompletion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages,
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
