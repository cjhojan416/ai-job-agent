import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "phi3",
    "prompt": "Improve this resume summary for a software developer.",
    "stream": False
}

response = requests.post(url, json=data)

print(response.json()["response"])