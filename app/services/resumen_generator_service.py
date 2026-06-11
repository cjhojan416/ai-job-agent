from app.services.ai_service import ask_ai


def generate_optimized_resume(
    cv_text,
    job_description
):

    prompt = f"""
You are an expert resume writer.

Your task is to rewrite and improve the resume to better match the job description.

IMPORTANT RULES:
- Do NOT invent experience.
- Do NOT invent jobs.
- Do NOT invent certifications.
- Do NOT invent degrees.
- Keep all information truthful.
- Improve wording and structure.
- Highlight relevant skills and achievements.
- Optimize the resume for ATS systems.

Return ONLY the optimized resume.

RESUME:
{cv_text}

JOB DESCRIPTION:
{job_description}
"""

    response = ask_ai(prompt)

    return response