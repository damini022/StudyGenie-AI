import google.generativeai as genai

def generate_notes(model, text):

    prompt = f"""
You are an expert teacher.

Read the following study material and generate:

1. Short Notes
2. Important Points
3. Key Definitions

Study Material:

{text}
"""

    response = model.generate_content(prompt)

    return response.text