import streamlit as st

from utils.gemini import model
from utils.planner import generate_study_plan

st.title("📅 AI Study Planner")

# Check if PDF is uploaded
if "pdf_text" not in st.session_state:
    st.warning("⚠️ Please upload a PDF from the Home page first.")
    st.stop()

pdf_text = st.session_state["pdf_text"]

# Show uploaded file name
st.success(f"📄 Current PDF: {st.session_state['file_name']}")

exam_date = st.date_input("📅 Select Exam Date")

study_hours = st.slider(
    "⏰ Daily Study Hours",
    min_value=1,
    max_value=12,
    value=4
)

if st.button("Generate Study Plan"):

    with st.spinner("Creating Study Plan..."):

        plan = generate_study_plan(
            model,
            pdf_text,
            exam_date,
            study_hours
        )

    st.success("✅ Study Plan Generated Successfully!")

    st.write(plan)