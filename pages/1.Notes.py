import streamlit as st
from utils.pdf_generator import create_pdf
from utils.gemini import model
from utils.notes import generate_notes

st.title("📝 AI Notes Generator")

# Check if PDF is uploaded
if "pdf_text" not in st.session_state:
    st.warning("⚠️ Please upload a PDF from the Home page first.")
    st.stop()

pdf_text = st.session_state["pdf_text"]

# Show uploaded file name
st.success(f"📄 Current PDF: {st.session_state['file_name']}")

# Preview PDF Text
with st.expander("📖 Preview PDF"):
    st.write(pdf_text[:1000])

# Generate Notes
if st.button("Generate Notes"):

    with st.spinner("Generating Notes..."):
        notes = generate_notes(model, pdf_text)

    st.success("✅ Notes Generated Successfully!")
    st.write(notes)

    pdf_file = create_pdf(notes)

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="📥 Download Notes as PDF",
            data=file,
            file_name="StudyGenie_Notes.pdf",
            mime="application/pdf"
        )