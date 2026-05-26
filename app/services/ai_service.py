import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_ollama(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def improve_cv(cv_text):

    prompt = f"""
    Analiza y mejora este CV.

    REGLAS ESTRICTAS:

    - NO cambies el nombre de la persona
    - NO traduzcas el CV
    - MANTÉN el idioma original
    - MANTÉN toda la información personal exactamente igual
    - NO modifiques correos electrónicos
    - NO modifiques teléfonos
    - NO inventes información
    - NO cambies empresas
    - NO cambies tecnologías
    - SOLO mejora redacción y estructura
    - Optimizado para ATS
    - Formato profesional

    CV:
    {cv_text}
    """

    return ask_ollama(prompt)

