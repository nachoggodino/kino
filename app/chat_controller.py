from fastapi import APIRouter
from app.schema.schema import PromptRequest, ResponsePayload, TokenRequest, TokenResponsePayload
from app.chat_service import handle_prompt, handle_tokens

router = APIRouter()

@router.post("/chat", response_model=ResponsePayload)
def chat_endpoint(request: PromptRequest):
    return handle_prompt(request.prompt, request.model)

@router.post("/tokenize", response_model=TokenResponsePayload)
def tokenize_endpoint(request: TokenRequest):
    return handle_tokens(request.prompt, request.model)