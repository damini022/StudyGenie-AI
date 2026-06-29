def ask_pdf(model, pdf_text, question):

    prompt = f"""
You are a study assistant.

Only answer using the information provided below.

If the answer is not present in the study material, reply:
"I could not find this in the uploaded PDF."

Study Material:

{pdf_text}

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text