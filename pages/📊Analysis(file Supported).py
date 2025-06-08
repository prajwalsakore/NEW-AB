import streamlit as st
import pandas as pd

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Lead Conversion Predictor", layout="wide")

# ---------- CUSTOM STYLING (LIGHT BACKGROUND) ----------
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background: linear-gradient(to bottom right, #ffffff, #e6f2ff);
        padding: 2rem;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🔍 Lead Conversion Predictor")
st.write("Upload a lead CSV file and get predictions on who might convert to a customer.")

# ---------- FILE UPLOAD ----------
uploaded_file = st.file_uploader("📂 Upload your lead CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Rename columns if needed
    expected_cols = ['First Name', 'Last Name', 'Email', 'Interest', 'City', 'Phone', 'Source']
    df.columns = expected_cols[:len(df.columns)]

    # ---------- PREDICTION RULE FUNCTION ----------
    def predict_lead(row):
        interest_keywords = ['AI', 'Marketing', 'SEO', 'Tools']
        high_quality_sources = ['TechVerse', 'Rankify', 'BuzzHub']

        interest_match = any(keyword.lower() in str(row['Interest']).lower() for keyword in interest_keywords)
        source_match = str(row['Source']).strip() in high_quality_sources

        if interest_match and source_match:
            return "✅ Likely to Convert"
        elif interest_match or source_match:
            return "🤔 Possible Conversion"
        else:
            return "❌ Unlikely to Convert"

    # Apply prediction
    df['Prediction'] = df.apply(predict_lead, axis=1)

    # ---------- DISPLAY RESULT TABLE ----------
    st.success("✅ Predictions generated successfully!")
    st.markdown("### 📊 Lead Analysis Table")

    styled_df = df.style.applymap(
        lambda val: 'color: green; font-weight: bold;' if 'Likely' in str(val) else (
                    'color: orange; font-weight: bold;' if 'Possible' in str(val) else (
                    'color: red; font-weight: bold;' if 'Unlikely' in str(val) else ''))
        , subset=['Prediction']
    )

    st.dataframe(styled_df, use_container_width=True)
    # -- CSV Download --
import io
csv_buffer = io.StringIO()
df.to_csv(csv_buffer, index=False)
csv_data = csv_buffer.getvalue()

st.download_button(
    label="📥 Download Predictions as CSV",
    data=csv_data,
    file_name="lead_predictions.csv",
    mime="text/csv"
)

else:
    st.info("Upload a CSV with columns like: First Name, Last Name, Email, Interest, City, Phone, Source.")

