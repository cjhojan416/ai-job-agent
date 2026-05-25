from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(text, output_path):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    content = []

    paragraphs = text.split("\n")

    for p in paragraphs:
        content.append(Paragraph(p, styles["BodyText"]))
        content.append(Spacer(1, 12))

    doc.build(content)