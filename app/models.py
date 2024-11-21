from typing import List
from datetime import datetime
from pydantic import BaseModel

class MessageRequest(BaseModel):
    message: str
    topic: str

class MessageResponse(BaseModel):
    id: str
    message: str
    topic: str
    last_updated: datetime

class ChannelRequest(BaseModel):
    topic: List[str]

class ChannelResponse(BaseModel):
    id: str
    topic: List[str]
