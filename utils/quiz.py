import json

def generate_quiz(model, pdf_text):

    prompt = f"""
You are an expert teacher.

Read the study material below.

Generate EXACTLY 10 multiple choice questions.

Return ONLY a valid JSON array.

Format:

[
  {{
    "question":"...",
    "options":[
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer":"Option B"
  }}
]

Rules:
- Exactly 10 questions
- 4 options only
- Only one correct answer
- Easy to Medium level
- Do NOT write markdown
- Do NOT write ```json
- Return ONLY JSON

Study Material:

{pdf_text}
"""

    response = model.generate_content(prompt)

    quiz = json.loads(response.text)

    return quiz