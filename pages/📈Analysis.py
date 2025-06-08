import streamlit as st
import openai

# Set page config
st.set_page_config(page_title="Lead Conversion Classifier", layout="wide")

# ✅ Set OpenAI Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ✅ Custom Page Background (optional)
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background: linear-gradient(to bottom right, #fefcea, #f1da36);
        padding: 2rem;
    }
    .block {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ UI
st.title("🔍 Lead Conversion Classifier")
st.write("Predict whether a lead is likely to convert into a customer based on their information.")

st.markdown("### 🧾 Enter Lead Details")

with st.form("lead_form"):
    name = st.text_input("Name of Lead")
    age = st.number_input("Age", 18, 100, 25)
    location = st.text_input("Location")
    budget = st.text_input("Approx. Budget / Spending Potential (INR)")
    product_interest = st.text_area("Product/Service of Interest")
    urgency = st.selectbox("Urgency Level", ["Very Urgent", "Somewhat Interested", "Just Exploring"])
    interaction_level = st.selectbox("Interaction So Far", ["Multiple Calls/Meetings", "One Demo Given", "Only One Call", "None"])
    
    submitted = st.form_submit_button("🚀 Predict Conversion")

if submitted:
    with st.spinner("Predicting using AI..."):
        prompt = f"""
You are a business assistant. Based on the following lead data, classify the chance of conversion into 3 categories: 
1. High chance ✅ 
2. Medium chance ⚠️ 
3. Low chance ❌ 
Also, briefly explain why.

Name: {name}
Age: {age}
Location: {location}
Budget: {budget}
Interest: {product_interest}
Urgency: {urgency}
Interaction Level: {interaction_level}
"""
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        result = response.choices[0].message.content

        # ✅ Output in Card
              st.markdown("### 🧠 AI Prediction Result")
        st.markdown(f"""
        <div class='block'>
            <h4>📈 Prediction Summary:</h4>
            <div style="font-size:1.1rem;">{result}</div>
        </div>
        """, unsafe_allow_html=True)

