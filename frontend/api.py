import requests

BASE_URL = "http://localhost:8000/kino"

def api_chat(prompt: str, model: str) -> str:
    payload = {"prompt": prompt, "model": model}
    response = requests.post(f"{BASE_URL}/chat", json=payload)
    return response.json()["response"]

def api_tokenize(prompt: str, model: str) -> dict:
    payload = {"prompt": prompt, "model": model}
    response = requests.post(f"{BASE_URL}/tokenize", json=payload)
    return response.json()

