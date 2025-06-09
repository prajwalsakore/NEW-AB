import streamlit as st
import openai
import os

# Set your OpenAI API key securely (use Streamlit secrets in production)
openai.api_key = os.getenv("OPENAI_API_KEY") or "your-api-key-here"

# Set Streamlit page config
st.set_page_config(page_title="📞 AI Chatbot Assistant", layout="centered")

st.title("🤖 Smart Chatbot Assistant")
st.write("Ask anything about how to use the app!")

# System prompt defining how the bot should behave
system_prompt = """
You are a friendly and intelligent assistant inside a web app that helps users with digital content generation, SEO scoring, and lead prediction.

Here’s how the app works:

1. Users log in and see a welcome message.
2. The "Generate" section lets users create:
   - Blogs
   - Instagram captions
   - YouTube video scripts
3. The "SEO Checker" allows users to paste a blog and receive an SEO score out of 100 with suggestions.
4. In the "Analysis" section, users can:
   - Enter single lead details manually to check conversion possibility.
   - Upload a CSV file containing leads and get predictions with a downloadable result.
5. "User Info" shows their email, full name, and role.
6. "Chatbot" (You) help users understand and navigate the app.
7. "Plans and Billing" shows available plans (Basic, Pro, Premium) and dummy payment options.

Always give answers based only on this app's layout and features. Never mention sections like "Content Creation" or "Blog Tool" that don't exist.

Example:  
If a user asks “Where can I generate a blog?”, reply:  
👉 “You can generate blogs by going to the **Generate** section of the app.”

Be brief, clear, and specific to this app.
"""

# Session state to hold chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("💬 Ask something about the app:", key="chat_input")

if user_input:
    with st.spinner("Generating response..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    *st.session_state.chat_history,
                    {"role": "user", "content": user_input}
                ]
            )
            bot_reply = response.choices[0].message["content"]

            # Update chat history
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

        except Exception as e:
            bot_reply = f"❌ Error: {str(e)}"

    # Display bot response
    st.markdown("**🧠 Assistant:**")
    st.info(bot_reply)

# Display chat history (optional)
if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("🕘 Chat History")
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")

