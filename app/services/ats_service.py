from app.services.ai_service import ask_ollama


def analyze_cv_match(cv_text, job_description):

    prompt = f"""
You are an ATS resume analyzer.

Analyze this resume against the job description.

Return:
1. Match percentage
2. Missing skills
3. Strengths
4. Weaknesses
5. Suggestions to improve the resume

RESUME:
{cv_text}

JOB DESCRIPTION:
{job_description}
"""

    response = ask_ollama(prompt)

    return response