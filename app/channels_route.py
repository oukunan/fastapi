from fastapi import APIRouter, HTTPException
from channels_crud import get_all_channels, update_channel, get_channel_by_id
from models import ChannelRequest

channel_route = APIRouter()

@channel_route.get("/channels")
def get_channels():
    return get_all_channels()

@channel_route.put("/channels/{id}", status_code=200)
def update_channel_topics(channel_id: str, request: ChannelRequest):
    if not get_channel_by_id(channel_id):
        raise HTTPException(status_code=404, detail="Channel not found")
    
    update_channel(channel_id, request.dict())
    return {"detail": "Updated successfully"}
