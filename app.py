import streamlit as st
from transformers import pipeline

# Page title
st.set_page_config(page_title="AI Text Summarizer", layout="centered")
st.title("📝 AI Text Summarizer")
st.markdown("Summarize any text using Hugging Face Transformers.")

# Load the summarization pipeline
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# Text input
input_text = st.text_area("Enter your text here:", height=300)

# Button to summarize
if st.button("Summarize"):
    if not input_text.strip():
        st.warning("⚠️ Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(input_text, max_length=100, min_length=30, do_sample=False)
            st.subheader("Summary:")
            st.success(summary[0]['summary_text'])