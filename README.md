# 📚 StudyGenie AI

An AI-powered Study Assistant built using **Python, Streamlit, and Google Gemini AI** that helps students study smarter from PDFs.

---

## 🚀 Features

- 📄 Upload Study PDF
- 📝 AI Notes Generator
- ❓ Ask Questions from PDF
- 📖 AI Quiz Generator
- 🧠 AI Flashcards
- 📅 AI Study Planner
- 📥 Download Notes as PDF
- 💻 Interactive Streamlit UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- ReportLab
- PyPDF2
- python-dotenv

---

## 📂 Project Structure

```
StudyGenie-AI/
│
├── app.py
├── pages/
│   ├── Notes.py
│   ├── Quiz.py
│   ├── Flashcard.py
│   ├── Planner.py
│   └── AskAI.py
│
├── utils/
│   ├── gemini.py
│   ├── notes.py
│   ├── quiz.py
│   ├── flashcard.py
│   ├── planner.py
│   ├── chatbot.py
│   ├── pdf_generator.py
│   └── pdf_reader.py
│
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/damini022/StudyGenie-AI.git
```

Move into the project

```bash
cd StudyGenie-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---











---

## 🎯 Future Improvements

- RAG using FAISS
- Chat History
- Voice Assistant
- Multi-language Support

---

## 👩‍💻 Author

**Damini Rathore**

IGDTUW | Information Technology
