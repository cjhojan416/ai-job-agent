from io import BytesIO
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from app.services.ai_service import ask_ollama

def generate_optimized_cv(cv_text, job_description):

    prompt = f"""
You are a professional resume writer.

Rewrite and optimize this resume for the job description.

Rules:
- Keep it professional
- ATS friendly
- Improve wording
- Add strong action verbs
- Highlight relevant skills
- Keep a clean structure

Return ONLY the improved resume text.

RESUME:
{cv_text}

JOB DESCRIPTION:
{job_description}
"""

    optimized_cv = ask_ollama(prompt)

    return optimized_cv



def create_pdf(cv_content):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    for line in cv_content.split("\n"):

        if line.strip():

            elements.append(
                Paragraph(line, styles['BodyText'])
            )

            elements.append(
                Spacer(1, 12))

    doc.build(elements)

    buffer.seek(0)

    return buffer