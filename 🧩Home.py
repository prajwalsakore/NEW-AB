

import streamlit as st
import utils

# At the top (after imports), initialize session_state
if "user_info_submitted" not in st.session_state:
    st.session_state.user_info_submitted = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "user_role" not in st.session_state:
    st.session_state.user_role = ""

# Inside your "User Info" page or "Home" section
if not st.session_state.user_info_submitted:
    st.title("👤 User Info")
    st.markdown("Please fill in your details to proceed:")

    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    role = st.selectbox("Select Your Role", ["Marketer", "Student", "Content Creator"])

    if st.button("Submit"):
        if full_name and email:
            st.session_state.user_info_submitted = True
            st.session_state.user_name = full_name
            st.session_state.user_role = role
        else:
            st.warning("Please enter all fields.")
else:
    st.success(f"👋 Welcome, {st.session_state.user_name} ({st.session_state.user_role})")
    st.markdown("### 🎯 Here’s your personalized dashboard:")
    st.markdown("- 🔥 Go to Generate tab to create content.")
    st.markdown("- 💡 Visit Content Ideas to get fresh topics.")
    st.markdown("- 🧾 Manage your subscription in Billing.")


# Set page config
st.set_page_config(page_title="AI Content Generator", page_icon="✨", layout="centered")

# Dark-mode-compatible custom CSS
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        color: #E1E1E1 !important;
        background-color: #0E1117 !important;
    }

    .stTextInput input {
        background-color: #262730;
        color: #E1E1E1;
        border: 1px solid #565656;
        border-radius: 0.5rem;
        padding: 0.5rem;
    }

    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #262730;
        color: #E1E1E1;
        border-radius: 0.5rem;
    }

    .stButton>button {
        background-color: #4f46e5;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
        border: none;
        transition: background 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #3730a3;
    }

    .block {
        background-color: #1E1F25;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.4);
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# UI content
st.markdown("## ✨ Welcome to AI Content Generator")
st.write("Create engaging **blogs**, **emails**, and **captions** effortlessly with the power of AI.")

with st.container():
    st.markdown("### 👤 Enter Your Details")
    with st.container():
        st.markdown('<div class="block">', unsafe_allow_html=True)

        username = st.text_input("Enter your Username")
        email = st.text_input("Enter your Email")
        role = st.selectbox("What best describes you?", ["Student", "Marketer", "Content Creator", "Business Owner", "Other"])

        if st.button("🚀 Submit"):
            if username and email:
                utils.store_user_info(username, email, role)
                st.success("✅ Your info has been saved!")
            else:
                st.warning("⚠️ Please enter both Username and Email.")

        st.markdown('</div>', unsafe_allow_html=True)

