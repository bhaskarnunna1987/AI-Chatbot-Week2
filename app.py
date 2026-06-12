import streamlit as st
import json

# Load intents
with open("intents.json", "r") as file:
    intents = json.load(file)

# App title
st.title("AI Chatbot")

# Store conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Enter your message")

# Process input
if st.button("Send"):

    response = "Sorry, I don't understand that."

    for key in intents:
        if key in user_input.lower():
            response = intents[key]
            break

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display chat history
for sender, message in st.session_state.history:
    st.write(f"**{sender}:** {message}")