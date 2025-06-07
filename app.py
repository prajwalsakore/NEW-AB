
import streamlit as st
import utils

st.set_page_config(page_title="AI Content Generator", layout="centered")

st.title("🚀 Welcome to AI Content Tool")

# Collect user data
username = st.text_input("Enter your Username")
email = st.text_input("Enter your Email")
role = st.selectbox("Select your Role", ["Student", "Marketer", "Content Creator", "Business Owner", "Other"])

if st.button("Submit"):
    if username and email:
        utils.store_user_info(username, email, role)
        st.success("Your information has been saved!")
    else:
        st.warning("Please enter both username and email.")
