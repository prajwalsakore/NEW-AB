import streamlit as st
import json
import os

st.set_page_config(page_title="User Info", page_icon="🧑‍💼")

st.markdown("## 🧾 Your Profile Information")

# Load stored user info from JSON file
user_file = "user_info.json"

if os.path.exists(user_file):
    with open(user_file, "r") as f:
        user_data = json.load(f)

    st.markdown("### 📇 Your Details")
    st.write(f"**👤 Username:** {user_data.get('username', 'N/A')}")
    st.write(f"**📧 Email:** {user_data.get('email', 'N/A')}")
    st.write(f"**🧠 Role:** {user_data.get('role', 'N/A')}")
    st.write(f"**💼 Current Plan:** {user_data.get('plan', 'Free')}")  # You can dynamically set plan later

else:
    st.warning("⚠️ No user data found. Please go to the Home page and submit your details.")
