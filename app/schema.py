from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class ResponsePayload(BaseModel):
    response: str
