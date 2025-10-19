import streamlit as st
import requests
import json

BASE_URL = "http://localhost:8000"

st.title("Kino Chat Debugger")

# Input
prompt = st.text_input("Enter a prompt:")
model = st.selectbox("Choose a model", [
    "nous-hermes2:10.7b-solar-fp16",
    "wizardlm-uncensored:13b-llama2-fp16",
    "dolphin3:8b-llama3.1-fp16"
])
send = st.button("Send")

# Request + Response
if send and prompt:
    payload = {"prompt": prompt, "model": model}
    response = requests.post(f"{BASE_URL}/chat/", json=payload)

    st.subheader("📤 Request Payload")
    st.json(payload)

    st.subheader("📥 Raw Response")
    try:
        st.json(response.json())
    except Exception:
        st.text(response.text)
