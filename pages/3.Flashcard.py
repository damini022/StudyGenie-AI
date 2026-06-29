import streamlit as st

from utils.gemini import model
from utils.flashcard import generate_flashcards

st.title("🧠 AI Flashcards")

# Check if PDF is uploaded
if "pdf_text" not in st.session_state:
    st.warning("⚠️ Please upload a PDF from the Home page first.")
    st.stop()

pdf_text = st.session_state["pdf_text"]

# Show uploaded file name
st.success(f"📄 Current PDF: {st.session_state['file_name']}")

# Generate Flashcards
if st.button("Generate Flashcards"):

    with st.spinner("Generating Flashcards..."):

        flashcards = generate_flashcards(model, pdf_text)

    st.success("✅ Flashcards Generated Successfully!")

    st.write(flashcards)