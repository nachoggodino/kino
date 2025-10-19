from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str
    model: str

class ResponsePayload(BaseModel):
    response: str
