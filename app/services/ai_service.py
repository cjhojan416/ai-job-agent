import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_cv(cv_text):

    prompt = f"""
    Analiza este CV y ​​devuelve ÚNICAMENTE JSON.

        REGLAS ESTRICTAS:

        - NO cambies el nombre de la persona
        - NO traduzcas el CV
        - MANTÉN el idioma original
        - MANTÉN toda la información personal exactamente igual
        - NO modifiques las direcciones de correo electrónico
        - NO modifiques los números de teléfono
        - NO inventes información
        - NO cambies los nombres de las empresas
        - NO cambies las tecnologías
        - SOLO mejora la redacción y la estructura
        - Mantén la información veraz
        - Optimizado para ATS
        - Formato profesional

    CV:
    {cv_text}
    """

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
    Improve this CV professionally.

    Requirements:
    - Better wording
    - ATS optimized
    - Professional language
    - Highlight achievements
    - Keep information truthful
    - Return clean structured text

    CV:
    {cv_text}
    """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]