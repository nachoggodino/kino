from app.chat_model import query_model
from app.utils.preprocess import build_prompt
from app.schema.chat_history import ChatHistory
from app.schema.schema import ResponsePayload, TokenResponsePayload
from app.utils.tokenize import get_model_max_context, count_tokens

chat_history = ChatHistory(10)

def handle_prompt(prompt: str, model) -> dict:
    # Retrieve chat history
    history_formatted = chat_history.format()
    # Preprocess
    full_prompt = build_prompt(prompt, history_formatted)
    # Call model
    response = query_model(full_prompt, model)
    # Update chat history
    chat_history.add(prompt, response)
    return ResponsePayload(response=response)

def handle_tokens(prompt: str, model: str) -> dict:
    full_prompt = build_prompt(prompt, chat_history.format())
    token_count = count_tokens(full_prompt, model)
    max_context = get_model_max_context(model)
    return TokenResponsePayload(tokens=token_count, max_context=max_context)
