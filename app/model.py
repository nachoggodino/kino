import requests

def query_model(prompt: str, model: str = "wizardlm:13b-fp16") -> str:
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]
