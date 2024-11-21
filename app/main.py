from fastapi import FastAPI
from .messages_route import message_router
from .channels_route import channel_route

app = FastAPI()

app.include_router(message_router)
app.include_router(channel_route)
