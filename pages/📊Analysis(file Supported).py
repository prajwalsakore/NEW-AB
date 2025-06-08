import streamlit as st
import pandas as pd

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Lead Conversion Predictor", layout="wide")


# ---------- CUSTOM LIGHT BACKGROUND ----------
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background: linear-gradient(to bottom right, #ffffff, #e0eaff);
        padding: 2rem;
    }
    .card {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .positive {
        color: green;
        font-weight: bold;
    }
    .negative {
        color: red;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🔍 Lead Conversion Predictor")
st.markdown("Upload your lead CSV to get smart predictions based on interest and source.")

# ---------- FILE UPLOAD ----------
uploaded_file = st.file_uploader("Upload your lead CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # ---------- BASIC RULE-BASED MODEL ----------
    def predict_lead(row):
        interest_keywords = ['AI', 'Marketing', 'SEO', 'Tools']
        high_quality_sources = ['TechVerse', 'Rankify', 'BuzzHub']

        interest_match = any(keyword.lower() in str(row['Interest']).lower() for keyword in interest_keywords)
        source_match = str(row['Source']).strip() in high_quality_sources

        if interest_match and source_match:
            return "Likely to Convert ✅"
        elif interest_match or source_match:
            return "Possible Conversion 🤔"
        else:
            return "Unlikely to Convert ❌"

    # Rename columns if needed
    expected_cols = ['First Name', 'Last Name', 'Email', 'Interest', 'City', 'Phone', 'Source']
    df.columns = expected_cols[:len(df.columns)]

    # Make predictions
    df['Prediction'] = df.apply(predict_lead, axis=1)

    # ---------- DISPLAY LEAD CARDS ----------
    st.subheader("📋 Lead Predictions")

    for index, row in df.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="card">
                <h4>👤 {row['First Name']} {row['Last Name']}</h4>
                <p><strong>Email:</strong> {row['Email']}</p>
                <p><strong>Interest:</strong> {row['Interest']}</p>
                <p><strong>City:</strong> {row['City']}</p>
                <p><strong>Source:</strong> {row['Source']}</p>
                <p><strong>Prediction:</strong> 
                <span class="{ 'positive' if 'Likely' in row['Prediction'] else 'negative' if 'Unlikely' in row['Prediction'] else ''}">
                {row['Prediction']}</span></p>
            </div>
            """, unsafe_allow_html=True)
else:
    st.info("📂 Upload a CSV file to begin. Make sure it has columns like: First Name, Last Name, Email, Interest, City, Phone, Source.")

