import streamlit as st
from utils.prompt_loader import load_prompt
from utils.ai_engine import run_prompt

st.set_page_config(page_title="IdeaSnap", layout="centered")
st.title("💡 IdeaSnap — Your AI Co-Founder")
st.markdown("Enter your startup idea below. IdeaSnap will generate a SWOT analysis using AI.")

# Startup idea input
idea = st.text_area("Describe your startup idea:", height=200)

if st.button("Generate SWOT Analysis"):
    if not idea.strip():
        st.warning("Please enter a startup idea.")
    else:
        with st.spinner("Analyzing your idea with AI..."):
            try:
                prompt_template = load_prompt("swot")
                result = run_prompt(prompt_template, {"idea": idea})
                st.subheader("📊 SWOT Analysis")
                st.write(result)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
