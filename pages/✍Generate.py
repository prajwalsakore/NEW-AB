import streamlit as st
import openai

# --- Page Setup ---
st.set_page_config(page_title="Generate Content", layout="wide")
# Custom Page Background
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
background: linear-gradient(to bottom right, #fdfbfb, #ebedee);
background-size: cover;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
##
st.title("✍️ AI Content Generator")

# --- OpenAI Key ---
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- CSS for Card Layout ---
st.markdown("""
<style>
.card {
    background-color: #1E1F25;
    padding: 1.5rem;
    border-radius: 1rem;
    box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    margin-bottom: 1.5rem;
}
.card h4 {
    color: #A5B4FC;
}
</style>
""", unsafe_allow_html=True)

# --- User Input ---
options = ["Blog", "Caption", "Email", "Content Ideas", "Video Scripts"]
choice = st.selectbox("🧠 Choose what you want to generate:", options)

prompt = st.text_area("💡 Enter your topic or idea here")

# --- Generate Content ---
if st.button("🚀 Generate Content"):
    if prompt:
        with st.spinner("Generating using AI..."):
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": f"Write a {choice.lower()} on: {prompt}"}],
                    max_tokens=800
                )
                generated_text = response.choices[0].message.content.strip()

                # Display in Card Format
                st.markdown("### 🎯 AI-Generated Result")
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown('<div class="card"><h4>📝 Type</h4>', unsafe_allow_html=True)
                    st.markdown(f"<p><b>{choice}</b></p>", unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with col2:
                    st.markdown('<div class="card"><h4>🔍 Topic</h4>', unsafe_allow_html=True)
                    st.markdown(f"<p>{prompt}</p>", unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                with col3:
                    st.markdown('<div class="card"><h4>✨ Output</h4>', unsafe_allow_html=True)
                    st.markdown(f"<div style='white-space: pre-wrap;'>{generated_text}</div>", unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"⚠️ An error occurred: {e}")
    else:
        st.warning("❗ Please enter a topic first.")
