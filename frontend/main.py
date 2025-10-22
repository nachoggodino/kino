import streamlit as st
import requests

from frontend.models import MODEL_MAP
from frontend.ui_util import avatar, get_author, log_to_console
from frontend.api import api_chat, api_tokenize

BASE_URL = "http://localhost:8000/kino"
USER_ROLE = "nacho"
KINO_ROLE = "kino"
st.title("Kino Chat")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Model selection
col1, col2 = st.columns([2, 1])
with col1:
    selected_name = st.selectbox("Choose a model", list(MODEL_MAP.keys()))
    model_info = MODEL_MAP[selected_name]
    model = model_info["model"]
with col2:
    st.metric("Context Limit", f"{model_info['context']} tokens")

# Display chat messages from history on app rerun
for message in st.session_state.chat_history:
    with st.chat_message(message["role"], avatar=avatar(message)):
        st.markdown(get_author(message["role"]) + message["content"])

# Placeholder for token usage progress bar
progress_placeholder = st.empty()

# Request + Response
if prompt := st.chat_input("Type your message and hit Enter"):
    # Trigger token count backend call
    token_info = api_tokenize(prompt, model)

    # Display token usage
    usage_pct = min(token_info["tokens"] / token_info["max_context"], 1.0)
    progress_placeholder.progress(usage_pct, text=f"{token_info['tokens']} / {token_info['max_context']} tokens")

    # Display user message in chat message container
    with st.chat_message(USER_ROLE, avatar=avatar(USER_ROLE)):
        st.markdown(get_author(USER_ROLE) + prompt)

    # Add user message to chat history
    st.session_state.chat_history.append({"role": USER_ROLE, "content": prompt})

    # Trigger model response backend call
    reply = api_chat(prompt, model)

    # Display kino response in chat message container
    with st.chat_message(KINO_ROLE, avatar=avatar(KINO_ROLE)):
        st.markdown(get_author(KINO_ROLE) + reply)

    # Add kino response to chat history
    st.session_state.chat_history.append({"role": KINO_ROLE, "content": reply})
