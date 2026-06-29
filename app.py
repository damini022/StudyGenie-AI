import streamlit as st
from utils.pdf_reader import extract_text

st.set_page_config(
    page_title="StudyGenie AI",
    page_icon="📚",
    layout="wide"
)
st.markdown("""
<style>

/* Sidebar */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#4F46E5,#7C3AED);
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    height:50px;
    font-size:17px;
    font-weight:bold;
}

/* File uploader */
div[data-testid="stFileUploader"]{
    border:2px dashed #4F46E5;
    border-radius:15px;
    padding:15px;
}

/* Metric cards */
div[data-testid="stMetric"]{
    background:#F8FAFC;
    padding:15px;
    border-radius:15px;
    border:1px solid #E5E7EB;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background: linear-gradient(135deg,#4F46E5,#7C3AED);
padding:35px;
border-radius:18px;
text-align:center;
color:white;
margin-bottom:25px;
">

<h1 style="margin-bottom:10px;">📚 StudyGenie AI</h1>

<h3>Your Personal AI Study Assistant</h3>

<p>Generate Notes • Quiz • Flashcards • Study Planner • AI Chat</p>

</div>
""", unsafe_allow_html=True)
st.markdown("""
<div style="
background:#F8FAFC;
padding:20px;
border-radius:15px;
border:1px solid #E5E7EB;
margin-bottom:15px;
">

<h3>📄 Upload Study Material</h3>

<p>
Upload your PDF once and access all AI features from the sidebar.
</p>

</div>
""", unsafe_allow_html=True)

st.header("📄 Upload Your Study PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf_text = extract_text(uploaded_file)

    st.session_state["pdf_text"] = pdf_text
    st.session_state["file_name"] = uploaded_file.name

    st.success("✅ PDF Uploaded Successfully!")

    with st.expander("📖 Preview"):
        st.write(pdf_text[:1000])
        st.markdown("---")

st.subheader("🚀 AI Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="
    background:#ffffff;
    padding:20px;
    border-radius:15px;
    border:1px solid #ddd;
    ">
    <h4>📝 AI Notes</h4>
    <p>Generate smart notes from your PDF.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
background:linear-gradient(135deg,#EEF2FF,#FFFFFF);
padding:25px;
border-radius:18px;
box-shadow:0 8px 20px rgba(0,0,0,0.08);
border-left:6px solid #4F46E5;
margin-bottom:20px;
transition:0.3s;
">
    <h4>📖 AI Quiz</h4>
    <p>Create AI-generated quizzes instantly.</p>
    </div>
    """, unsafe_allow_html=True)

st.subheader("Your Personal AI Study Assistant")
st.markdown("---")

st.subheader("📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 PDF Uploaded", "1")

with col2:
    st.metric("🤖 AI Modules", "5")

with col3:
    st.metric("⚡ Powered By", "Gemini 2.5 Flash")

st.markdown("---")


st.markdown("""



""")

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}

div[data-testid="stFileUploader"] {
    border: 2px dashed #4CAF50;
    border-radius: 12px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)