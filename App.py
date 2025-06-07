import streamlit as st

# Page config
st.set_page_config(
    page_title="AI Content Genie",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for modern UI
st.markdown("""
    <style>
    /* Page Background */
    .main {
        background-color: #f9f9f9;
        padding: 2rem;
    }
    .block-container {
        padding: 2rem 1rem 2rem 1rem;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        font-size: 1.1em;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }

    /* Text Input */
    .stTextInput>div>input {
        border-radius: 10px;
        padding: 10px;
        font-size: 1em;
    }

    /* SelectBox */
    .stSelectbox>div>div {
        border-radius: 10px;
        padding: 10px;
        font-size: 1em;
    }

    /* Headers */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #2c3e50;
    }

    /* Sidebar */
    .css-1d391kg {
        background-color: #ffffff !important;
        border-right: 2px solid #f1f1f1;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar branding
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712100.png", width=80)
    st.markdown("## 🧠 AI Content Genie")
    st.markdown("### Navigation:")
    st.markdown("""
- 🏠 Home  
- ✍️ Generate  
- 💡 Content Ideas  
- 📊 User Info  
- 🧾 Plans and Billing  
- 🤖 Chatbot
    """)
    st.markdown("---")
    st.caption("🚀 Built with Streamlit + OpenAI")

# Placeholder for page-specific content
st.title("🧠 Page Title")
st.markdown("### Add your content here...")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Enter something...")
    with col2:
        st.selectbox("Select something...", ["Option 1", "Option 2"])

st.button("🚀 Submit")

import streamlit as st
import utils

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

