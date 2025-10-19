import pytest
import app.chat_service as chat_service

@pytest.fixture(autouse=True)
def mock_ollama(monkeypatch):
    def fake_query_model(prompt: str, model: str = "llama3") -> str:
        return f"Mocked response to: {prompt}"

    monkeypatch.setattr(chat_service, "query_model", fake_query_model)
