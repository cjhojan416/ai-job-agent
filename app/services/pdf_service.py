from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet



def generate_pdf(text, output_path):

    doc = SimpleDocTemplate(
        output_path,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    content = []

    paragraphs = text.split("\n")

    section_titles = [
        "SUMMARY",
        "EXPERIENCE",
        "EDUCATION",
        "SKILLS",
        "PROJECTS",
        "CERTIFICATIONS"
    ]

    for p in paragraphs:

        p = p.strip()

        if not p:
            continue

        # Detectar títulos
        if p.upper() in section_titles:

            title = Paragraph(
                f"<b>{p}</b>",
                styles["Heading2"]
            )

            content.append(title)
            content.append(Spacer(1, 12))

        else:

            body = Paragraph(
                p,
                styles["BodyText"]
            )

            content.append(body)
            content.append(Spacer(1, 10))

    doc.build(content)