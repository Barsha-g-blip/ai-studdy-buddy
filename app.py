import streamlit as st
from groq import Groq

# Initialize Groq client using Streamlit secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")

st.title("📚 AI Study Buddy")
st.write("Ask any academic question and get instant help!")

# User input
user_input = st.text_input("Enter your question:")

def ask_ai(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile"
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"

# When user submits question
if st.button("Ask"):
    if user_input:
        with st.spinner("Thinking..."):
            reply = ask_ai(user_input)
        st.success("Answer:")
        st.write(reply)
    else:
        st.warning("Please enter a question.")
