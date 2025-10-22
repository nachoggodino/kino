from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str
    model: str

class ResponsePayload(BaseModel):
    response: str

class TokenRequest(BaseModel):
    prompt: str
    model: str

class TokenResponsePayload(BaseModel):
    tokens: int
    max_context: int
