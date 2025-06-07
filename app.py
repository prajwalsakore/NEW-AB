import streamlit as st
import utils
from PIL import Image

st.set_page_config(page_title="AI Content Generator", page_icon="✨", layout="wide")

# --- Custom CSS for improved visual design ---
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .block-container {
        padding: 2rem;
        background-color: #ffffff;
        border-radius: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .stTextInput > div > input {
        padding: 0.5rem;
        border-radius: 0.5rem;
        border: 1px solid #d1d5db;
    }
    .stButton > button {
        background-color: #4f46e5;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        border: none;
        transition: background 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #3730a3;
    }
    </style>
""", unsafe_allow_html=True)

# --- App UI ---
st.markdown("## ✨ Welcome to AI Content Generator")
st.write("Create engaging **blogs**, **emails**, and **captions** effortlessly with the power of AI.")

with st.container():
    st.subheader("👤 Enter Your Details")
    username = st.text_input("Enter your Username")
    email = st.text_input("Enter your Email")
    role = st.selectbox("What best describes you?", ["Student", "Marketer", "Content Creator", "Business Owner", "Other"])

    if st.button("🚀 Submit"):
        if username and email:
            utils.store_user_info(username, email, role)
            st.success("✅ Your info has been saved!")
        else:
            st.warning("⚠️ Please enter both Username and Email.")

