import streamlit as st
import openai

# Get OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

# Function to generate text using OpenAI's ChatCompletion
def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a well-read journalist and are aware of the recent performance of India in Paralympics."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60  # Adjust token length as needed
    )
    return response.choices[0].message['content'].strip()

# Streamlit app layout
st.title("3daylive Chatbot")
st.write("Ask me anything")

# Create a chat container for the continuous stream
if "messages" not in st.session_state:
    st.session_state.messages = []

# Continuous chat input and response
user_input = st.chat_input("Enter your question here")

if user_input:
    # Display user input in the chat
    st.chat_message("user").write(user_input)

    # Generate AI response
    ai_response = generate_text(user_input)

    # Display AI response in the chat
    st.chat_message("assistant").write(ai_response)

    # Save the conversation
    st.session_state.messages.append({"user": user_input, "assistant": ai_response})

# Option to view entire conversation history
st.write("### Conversation History")
for message in st.session_state.messages:
    st.write(f"**User:** {message['user']}")
    st.write(f"**Assistant:** {message['assistant']}")
