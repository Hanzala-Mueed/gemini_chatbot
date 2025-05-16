import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="PakSeek AI", layout="centered")

st.title("🤖 PakSeek AI")

# User input section
with st.sidebar:
    st.header("User Settings")
    username = st.text_input("👤 Enter your username:", value=" ")
    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.text_input("Type your message...", key="input")

# When user sends message
if st.button("Send") and user_input.strip():
    try:
        response = requests.post("http://localhost:8000/chat", json={
            "username": username,
            "message": user_input
        })

        if response.status_code == 200:
            bot_reply = response.json().get("answer")

            # Fallback if Gemini returned None
            if not bot_reply:
                bot_reply = "⚠️ Gemini didn't return a response."

            # Store chat history
            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("bot", bot_reply))
        else:
            st.error(f"❌ Error {response.status_code}: Could not get a response from the chatbot.")
    except Exception as e:
        st.error(f"🚨 Server error: {e}")

# Display chat history
st.markdown("### 💬 Conversation")
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(
            f"<div style='text-align: right; color: #4e9af1; margin-bottom: 8px;'>🧑‍💻 <b>You:</b> {message}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='text-align: left; color: #31d843; margin-bottom: 8px;'>🤖 <b>Gemini:</b> {message}</div>",
            unsafe_allow_html=True
        )
