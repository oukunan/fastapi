from database import messages_collection, channels_collection
from datetime import datetime
from bson.objectid import ObjectId


def create_message_and_update_channel(payload):
    payload["last_updated"] = datetime.utcnow()

    message_creation_result = messages_collection.insert_one(payload)
    message_id = str(message_creation_result.inserted_id)

    topic = payload["topic"]
    message = payload["message"]

    existing_channel = channels_collection.find_one({"message": message})

    if existing_channel:
        channels_collection.update_one(
            {"message": message},
            {"$addToSet": {"topic": topic}},
        )
    else:
        channels_collection.insert_one(
            {"message": message, "topic": [topic]}
        )

    return message_id


def get_messages_by_message(message):
    messages = list(messages_collection.find({"message": message}))

    response = [
            {
                "id": str(message['_id']),
                "message": message["message"], 
                "topic": message["topic"],
                "last_updated": message["last_updated"]
            }
            for message in messages
    ]
    

    return response
