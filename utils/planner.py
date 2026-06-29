def generate_study_plan(model, pdf_text, exam_date, study_hours):

    prompt = f"""
You are an expert study mentor.

Based on the study material below, create a day-wise study plan.

Exam Date:
{exam_date}

Daily Study Hours:
{study_hours}

Requirements:
- Divide topics day-wise.
- Keep revision before exam.
- Mention important topics.
- Make the schedule realistic.

Study Material:

{pdf_text}
"""

    response = model.generate_content(prompt)

    return response.text