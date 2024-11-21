from fastapi import APIRouter, HTTPException
from app.crud.messages import get_messages_by_message, create_message_and_update_channel
from app.crud.channels import get_channel_by_id
from app.models import MessageRequest

router = APIRouter()


@router.post("/messages", status_code=201)
def post_message(request: MessageRequest):
    message_id = create_message_and_update_channel(request.dict())
    return {"id": message_id}


@router.get("/channels/{id}/messages")
def get_messages_by_channel(channel_id: str):
    channel = get_channel_by_id(channel_id)
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    return get_messages_by_message(channel["message"])