from pymongo.mongo_client import MongoClient
from config import settings

uri = settings.DATABASE_URL

client = MongoClient(uri)

db = client[settings.DATABASE_NAME]

messages_collection = db[settings.MESSAGES_COLLECTION_NAME]
channels_collection = db[settings.CHANNELS_COLLECTION_NAME]
