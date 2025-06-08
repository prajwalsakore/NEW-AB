
import streamlit as st
import utils

# --- Page Config ---
st.set_page_config(page_title="AI Content Generator", page_icon="✨", layout="centered")

# --- Background and Styling ---
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background: linear-gradient(to bottom right, #1a1a1a, #121212);
    background-size: cover;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
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
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Session State ---
if "user_info_submitted" not in st.session_state:
    st.session_state.user_info_submitted = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "role" not in st.session_state:
    st.session_state.role = ""

# --- Sidebar Navigation ---
page = st.sidebar.selectbox("📂 Navigate", ["🏠 Home", "🛠️ Generate", "ℹ️ About"])

# --- Home Page ---
if page == "🏠 Home":
    st.markdown("## ✨ Welcome to AI Content Generator")
    st.write("Create engaging **blogs**, **emails**, and **captions** effortlessly with the power of AI.")

    if not st.session_state.user_info_submitted:
        st.markdown("### 👤 Enter Your Details")
        st.markdown('<div class="block">', unsafe_allow_html=True)

        username = st.text_input("Enter your Username")
        email = st.text_input("Enter your Email")
        role = st.selectbox("What best describes you?", ["Student", "Marketer", "Content Creator", "Business Owner", "Other"])

        if st.button("🚀 Submit"):
            if username and email:
                utils.store_user_info(username, email, role)
                st.session_state.username = username
                st.session_state.role = role
                st.session_state.user_info_submitted = True
                st.success("✅ Your info has been saved!")
            else:
                st.warning("⚠️ Please enter both Username and Email.")

        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.success(f"👋 Welcome, {st.session_state.username} ({st.session_state.role})")
        st.markdown("### 🎯 Your Personalized Dashboard")
        st.markdown("- 🔥 Ready to generate content")
        st.markdown("- 💡 Explore fresh content ideas")
        st.markdown("- 🧾 Manage your subscription (Billing page coming soon)")

# --- Generate Page ---
elif page == "🛠️ Generate":
    st.title("🛠️ Generate AI Content")

    topic = st.text_input("Enter a topic or keyword")
    content_type = st.radio("Choose Content Type", ["Email", "Blog", "Social Media Caption"])

    if st.button("Generate"):
        if topic:
            # Simulated responses
            email_result = f"Subject: {topic}\nHi there, this is a marketing email about {topic}."
            blog_result = f"# Blog on {topic}\nThis blog explains the latest trends in {topic}."
            caption_result = f"🔥 Let's talk about {topic}! #trending"

            st.subheader("✨ Your Generated Content")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### 📧 Email")
                st.success(email_result if content_type == "Email" else "Not generated")

            with col2:
                st.markdown("#### 📝 Blog")
                st.info(blog_result if content_type == "Blog" else "Not generated")

            st.markdown("#### 📱 Social Caption")
            st.code(caption_result if content_type == "Social Media Caption" else "Not generated", language="markdown")
        else:
            st.warning("❗ Please enter a topic to generate content.")

# --- About Page ---
elif page == "ℹ️ About":
    st.title("ℹ️ About This Project")
    st.markdown("""
    **AI Content Generator** is an AI-powered content assistant that helps users generate:
    
    - ✉️ Emails  
    - 📄 Blogs  
    - 📱 Social Media Captions  

    ### 🔧 Technologies Used:
    - **OpenAI API**
    - **Streamlit**
    - **Custom Python Scripts**
    - **Session State for user login**

    ### 🎓 Created By:
    - **Prajwal Sakore**
    - Final Year, B.Tech (Your College)
    - For academic project submission

    ### 💡 Purpose:
    Help creators and marketers save time by generating high-quality content instantly using AI.
    """)


