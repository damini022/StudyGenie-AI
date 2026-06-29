import streamlit as st

from utils.gemini import model
from utils.quiz import generate_quiz

st.title("📖 AI Quiz")

if "pdf_text" not in st.session_state:
    st.warning("⚠️ Please upload a PDF from the Home page first.")
    st.stop()

pdf_text = st.session_state["pdf_text"]

st.success(f"📄 Current PDF: {st.session_state['file_name']}")

if st.button("Generate Quiz"):

    with st.spinner("Generating Quiz..."):

        st.session_state["quiz"] = generate_quiz(model, pdf_text)

if "quiz" in st.session_state:

    quiz = st.session_state["quiz"]

    st.subheader("📝 Quiz")

    score = 0

    for i, q in enumerate(quiz):

        st.markdown(f"### Question {i+1}")

        answer = st.radio(
            q["question"],
            q["options"],
            key=f"q{i}"
        )

        if answer == q["answer"]:
            score += 1

    if st.button("Submit Quiz"):

        st.success(f"🎉 Your Score: {score}/{len(quiz)}")

        percentage = (score / len(quiz)) * 100

        st.info(f"Percentage: {percentage:.1f}%")

        st.markdown("---")

        st.subheader("✅ Correct Answers")

        for i, q in enumerate(quiz):

            st.write(f"**Q{i+1}.** {q['question']}")

            st.success(f"✔ {q['answer']}")