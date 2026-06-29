from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile


def create_pdf(notes):

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    c = canvas.Canvas(temp_file.name, pagesize=letter)

    width, height = letter

    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "StudyGenie AI Notes")

    y -= 40

    c.setFont("Helvetica", 11)

    for line in notes.split("\n"):

        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 11)
            y = height - 50

        c.drawString(50, y, line[:100])

        y -= 18

    c.save()

    return temp_file.name