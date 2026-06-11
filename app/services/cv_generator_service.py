from io import BytesIO
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from app.services.ai_service import ask_ai

def generate_optimized_cv(cv_text, job_description):

    prompt = f"""
Eres un redactor profesional de currículums.

Reescribe y optimiza este currículum para la descripción del puesto.

Reglas:
- Mantén un tono profesional
- Compatible con sistemas ATS
- Mejora la redacción
- Añade verbos de acción contundentes
- Destaca las habilidades relevantes
- Mantén una estructura clara

Devuelve ÚNICAMENTE el texto del currículum mejorado.

RESUME:
{cv_text}

JOB DESCRIPTION:
{job_description}
"""

    optimized_cv = ask_ai(prompt)
    if not optimized_cv:
        raise ValueError(
        "La IA no devolvió contenido para generar el CV."
    )

    return optimized_cv



def create_pdf(cv_content):

    if not cv_content:
        raise ValueError(
            "No se recibió contenido para crear el PDF."
        )

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


