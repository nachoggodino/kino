import requests

BASE_URL = "http://localhost:8000"

def chat(prompt: str) -> str:
    response = requests.post(f"{BASE_URL}/chat/", json={"prompt": prompt})
    return response.json()["response"]
