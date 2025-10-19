# app/utils/formatting.py

def clean_prompt(prompt: str) -> str:
    # Basic cleanup for user input before sending to model.
    return prompt.strip()
