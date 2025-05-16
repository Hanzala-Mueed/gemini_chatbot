from pydantic import BaseModel
from datetime import datetime

class ChatBase(BaseModel):
    prompt: str
    response: str

class ChatCreate(ChatBase):
    user_id: int


class ChatRequest(BaseModel):
    username: str
    message: str

class ChatOut(ChatBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
