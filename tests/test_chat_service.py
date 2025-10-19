from app.chat_service import handle_prompt

def test_handle_prompt_returns_mocked_response():
    result = handle_prompt("Hello Kino")
    assert result["response"] == "Mocked response to: Hello Kino"
