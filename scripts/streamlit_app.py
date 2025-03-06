import streamlit as st
import requests

st.title("Bank Churn Prediction")

model = st.radio("Choose Model", ["CLV", "Churn"])
user_input = st.text_area("Enter customer data as JSON")

if st.button("Predict"):
    response = requests.post("https://your-api-id.execute-api.us-east-1.amazonaws.com/prod", json={"model": model.lower(), "data": eval(user_input)})
    st.json(response.json())