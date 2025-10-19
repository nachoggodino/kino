from fastapi import APIRouter
from app.schema import PromptRequest, ResponsePayload
from app.chat_service import handle_prompt

router = APIRouter()

@router.post("/", response_model=ResponsePayload)
def chat_endpoint(request: PromptRequest):
    return handle_prompt(request.prompt, request.model)
