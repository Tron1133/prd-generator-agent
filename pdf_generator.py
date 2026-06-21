from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

def create_pdf(content):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    for line in content.split("\n"):
        story.append(
            Paragraph(line, styles["BodyText"])
        )

    doc.build(story)

    buffer.seek(0)

    return buffer