import streamlit as st

st.title("Kino's Dumb Chatbot 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(("Bot", "Welcome to Kino's Dumb Chatbot! Type something below 👇"))

# Display chat history
for sender, message in st.session_state.messages:
    with st.chat_message(sender.lower()):
        st.markdown(message)

# Input box
user_input = st.chat_input("Say something to Kino:")

# Handle input
if user_input:
    st.session_state.messages.append(("You", user_input))
    # Dumb response logic
    if "hello" in user_input.lower():
        reply = "Hi there! I'm not very smart yet 😅"
    elif "bye" in user_input.lower():
        reply = "Goodbye! I’ll miss your nonsense 🥲"
    else:
        reply = f"I heard you say: '{user_input}' — fascinating!"
    st.session_state.messages.append(("Bot", reply))
