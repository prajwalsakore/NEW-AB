import streamlit as st
import openai

# 🧠 Setup
st.set_page_config(page_title="Lead Predictor", layout="wide")
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ✅ Dark-mode compatible styling
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background: linear-gradient(to bottom right, #0f2027, #203a43, #2c5364);
        padding: 2rem;
    }

    .block {
        background-color: #1e1e1e;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        color: #f1f1f1;
        margin-bottom: 2rem;
    }

    .stTextInput>div>input,
    .stTextArea>div>textarea,
    .stNumberInput>div>input,
    .stSelectbox>div>div {
        background-color: #2d2d2d;
        color: #ffffff;
        border: 1px solid #555;
        border-radius: 10px;
        padding: 0.6rem;
    }

    .stButton>button {
        background-color: #4f46e5;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        border: none;
        transition: background 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #3730a3;
    }
    </style>
""", unsafe_allow_html=True)

# 🧾 Title
st.title("📊 Lead Conversion Predictor")
st.write("Fill in lead details to predict if they'll convert into a customer.")

# 🧾 Input Fields
with st.container():
    st.markdown("<div class='block'>", unsafe_allow_html=True)

    name = st.text_input("Name of Lead")
    age = st.number_input("Age", min_value=18, max_value=100, value=25)
    interest = st.selectbox("Interest Level", ["High", "Medium", "Low"])
    budget = st.selectbox("Budget Range", ["<10K", "10K-50K", "50K-1L", "1L+"])
    channel = st.selectbox("Source Channel", ["Instagram", "Facebook", "Google Ads", "Referral", "Walk-In"])
    contact_count = st.slider("How many times you contacted?", 0, 10, 1)
    time_taken = st.slider("Response time (in hours)", 0, 72, 24)

    st.markdown("</div>", unsafe_allow_html=True)

# 🧠 AI Prediction
if st.button("Predict Lead Outcome 🚀"):
    if name:
        with st.spinner("Analyzing with AI..."):
            prompt = (
                f"Based on the following lead data, tell whether the lead is likely to convert into a customer and give a short reason:\n\n"
                f"Name: {name}\n"
                f"Age: {age}\n"
                f"Interest Level: {interest}\n"
                f"Budget: {budget}\n"
                f"Source: {channel}\n"
                f"Times Contacted: {contact_count}\n"
                f"Response Delay: {time_taken} hours"
            )

            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300
            )
            result = response.choices[0].message.content

            st.markdown("### 🧠 Prediction Result")
            st.markdown(f"""
            <div class='block'>
                <h4>📈 Prediction Summary:</h4>
                <div style="font-size:1.1rem;">{result}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Please enter the lead name.")


