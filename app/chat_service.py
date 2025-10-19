from app.model import query_model
from app.format import clean_prompt

def handle_prompt(prompt: str) -> dict:
    
    # Preprocess
    prompt = clean_prompt(prompt)

    # Call model
    response = query_model(prompt)

    # Postprocess (optional)
    return {"response": response}
