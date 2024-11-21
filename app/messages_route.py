from fastapi import APIRouter, HTTPException
from typing import List
from messages_crud import get_messages_by_message, create_message_and_update_channel
from channels_crud import get_channel_by_id
from models import MessageRequest, MessageResponse

message_router = APIRouter()


@message_router.post("/messages", status_code=201)
def post_message(request: MessageRequest):
    message_id = create_message_and_update_channel(request.dict())
    return {"id": message_id}


# @message_router.get("/channels/{id}/messages", response_model=List[MessageResponse])
@message_router.get("/channels/{id}/messages")
def get_messages_by_channel(id: str):
    channel = get_channel_by_id(id)
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    return get_messages_by_message(channel["message"])