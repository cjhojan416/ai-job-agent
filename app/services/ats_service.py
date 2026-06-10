from app.services.ai_service import ask_ollama


def analyze_cv_match(cv_text, job_description):

    prompt = f"""
You are a professional ATS resume analyzer.

Analyze the resume against the job description.

Respond ONLY in this format:



MISSING_SKILLS:
- skill 1
- skill 2

STRENGTHS:
- strength 1
- strength 2

WEAKNESSES:
- weakness 1
- weakness 2

SUGGESTIONS:
- suggestion 1
- suggestion 2


RESUME:
{cv_text}


JOB DESCRIPTION:
{job_description}
"""

    response = ask_ollama(prompt)

    return response