from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

print("API KEY:", os.getenv("OPENROUTER_API_KEY"))

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

response = client.chat.completions.create(
    model="nex-agi/nex-n2-pro:free",
    messages=[
        {
            "role": "user",
            "content": "Responde únicamente: Hola Mundo"
        }
    ]
)

print(response.choices[0].message.content)