import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Optional: print directly to verify
st.text("API KEY Loaded: " + str(os.getenv("OPENAI_API_KEY")))

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🧪 OpenAI API Key Test")

if st.button("Test OpenAI Call"):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": "Say hello in a cool way."}
            ],
            temperature=0.7,
        )
        st.success(response.choices[0].message.content)
    except Exception as e:
        st.error(f"❌ Error: {e}")
