from app.utils.preprocess import clean_prompt

def test_clean_prompt_basic():
    assert clean_prompt("  Hello  ") == "Hello"

def test_clean_prompt_empty():
    assert clean_prompt("   ") == ""

def test_clean_prompt_newlines():
    assert clean_prompt("\nHello\n") == "Hello"
