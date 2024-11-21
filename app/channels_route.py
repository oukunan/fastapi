from fastapi import APIRouter, HTTPException
from typing import List
from channels_crud import get_all_channels, update_channel, get_channel_by_id
from models import ChannelRequest, ChannelResponse

channel_route = APIRouter()

@channel_route.get("/channels")
def get_channels():
    return get_all_channels()

@channel_route.put("/channels/{id}", status_code=200)
def update_channel_topics(id: str, request: ChannelRequest):
    if not get_channel_by_id(id):
        raise HTTPException(status_code=404, detail="Channel not found")
    
    update_channel(id, request.dict())
    return {"detail": "Updated successfully"}
