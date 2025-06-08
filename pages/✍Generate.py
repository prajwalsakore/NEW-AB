
import streamlit as st
import openai

st.set_page_config(page_title="Generate Content", layout="wide")

st.title("✍️ AI Content Generator")

openai.api_key = st.secrets["OPENAI_API_KEY"]

options = ["Blog", "Caption", "Email", "Content Ideas","Video Scripts"]
choice = st.selectbox("Choose what you want to generate:", options)

prompt = st.text_area("Enter your topic or idea")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating..."):
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Write a {choice.lower()} on: {prompt}"}],
                max_tokens=800
            )
            st.markdown("### ✨ Output")
            st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter a topic first.")
