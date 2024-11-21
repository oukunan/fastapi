from fastapi import FastAPI
from .routes import channels, messages

app = FastAPI()

app.include_router(messages.router)
app.include_router(channels.router)
