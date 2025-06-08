
import streamlit as st

st.set_page_config(page_title="Plans and Billing", layout="wide")

st.title("📦 Plans and Billing")

menu = st.radio("Choose Section", ["Plan Details", "Billing"])

if menu == "Plan Details":
    st.subheader("🪙 Available Plans")
    st.info("**Basic Plan** – ₹0/month (Limited usage)")
    st.success("**Pro Plan** – ₹299/month (Unlimited text generation)")
    st.warning("**Premium Plan** – ₹599/month (Pro + Image + SEO tools)")

elif menu == "Billing":
    st.subheader("💳 Payment Portal")
    st.text_input("Name on Card")
    st.text_input("Card Number")
    st.text_input("Expiry Date")
    st.text_input("CVV")
    st.selectbox("Payment Gateway", ["Razorpay", "Paytm", "PhonePe", "Google Pay"])
    if st.button("Make Payment"):
        st.success("✅ Payment Successful! ")
