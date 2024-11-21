from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://admin:password1234@cluster0.0c4dc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

db = client["message_system"]

messages_collection = db["messages"]
channels_collection = db["channels"]
