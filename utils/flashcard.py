def generate_flashcards(model, pdf_text):

    prompt = f"""
You are an expert teacher.

Read the study material below.

Generate flashcards in this format:

Question:
Answer:

Generate at least 15 flashcards.

Study Material:

{pdf_text}
"""

    response = model.generate_content(prompt)

    return response.text