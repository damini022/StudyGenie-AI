import streamlit as st

from utils.gemini import model
from utils.chatbot import ask_pdf

st.title("❓ AI PDF Chatbot")

# Check if PDF is uploaded
if "pdf_text" not in st.session_state:
    st.warning("⚠️ Please upload a PDF from the Home page first.")
    st.stop()

pdf_text = st.session_state["pdf_text"]

# Show uploaded file name
st.success(f"📄 Current PDF: {st.session_state['file_name']}")

question = st.text_input("💬 Ask your question")

if st.button("Generate Answer"):

    if question.strip():

        with st.spinner("Thinking..."):

            answer = ask_pdf(model, pdf_text, question)

        st.success("✅ Answer Generated!")

        st.write(answer)

    else:
        st.warning("Please enter a question.")