from app.services.ai_service import ask_ai


def analyze_cv_match(cv_text, job_description):

    prompt = f"""

Eres un analista profesional de resúmenes de ATS.

Analiza el currículum comparándolo con la descripción del puesto.

Responde ÚNICAMENTE en este formato:

HABILIDADES QUE FALTAN:
- Habilidad 1
- Habilidad 2

FORTALEZAS:
- Fortaleza 1
- Fortaleza 2

DEBILIDADES:
- Debilidad 1
- Debilidad 2

SUGERENCIAS:
- Sugerencia 1
- Sugerencia 2


RESUME:
{cv_text}


JOB DESCRIPTION:
{job_description}
"""

    response = ask_ai(prompt)

    return response