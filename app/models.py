from typing import List
from pydantic import BaseModel

class MessageRequest(BaseModel):
    message: str
    topic: str

class ChannelRequest(BaseModel):
    topic: List[str]
