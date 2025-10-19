from app.model import query_model
from app.format import clean_prompt

def handle_prompt(prompt: str, model) -> dict:
    
    # Preprocess
    prompt = clean_prompt(prompt)

    # Call model
    response = query_model(prompt, model)

    # Postprocess (optional)
    return {"response": response}
