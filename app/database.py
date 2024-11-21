from pymongo.mongo_client import MongoClient
from .config import settings

username = settings.MONGO_INITDB_ROOT_USERNAME
password = settings.MONGO_INITDB_ROOT_PASSWORD

client = MongoClient(f"mongodb://{username}:{password}@mongo:27017")

db = client[settings.MONGO_INITDB_DATABASE]
messages_collection = db[settings.messages_collection_name]
channels_collection = db[settings.channels_collection_name]
