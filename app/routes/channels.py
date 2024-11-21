from fastapi import APIRouter, HTTPException
from app.crud.channels import get_all_channels, update_channel, get_channel_by_id
from app.models import ChannelRequest

router = APIRouter()

@router.get("/channels")
def get_channels():
    return get_all_channels()

@router.put("/channels/{id}", status_code=200)
def update_channel_topics(channel_id: str, request: ChannelRequest):
    if not get_channel_by_id(channel_id):
        raise HTTPException(status_code=404, detail="Channel not found")
    
    update_channel(channel_id, request.dict())
    return {"detail": "Updated successfully"}
