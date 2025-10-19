from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_endpoint_returns_mocked_response():
    response = client.post("/chat/", json={"prompt": "Hello Kino"})
    assert response.status_code == 200
    assert response.json()["response"] == "Mocked response to: Hello Kino"

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Kino backend is running"}