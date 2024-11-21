from bson.objectid import ObjectId
from app.database import channels_collection


def get_all_channels():
    channels = list(channels_collection.find())
    response = {
        "channels": [
            {
                "id": str(channel['_id']),
                "topic": channel["topic"]
            }
            for channel in channels
        ]
    }

    return response


def update_channel(channel_id, data):
    channels_collection.update_one({"_id": ObjectId(channel_id)}, {"$set": data})


def get_channel_by_id(channel_id):
    if not ObjectId.is_valid(channel_id):
        return None

    return channels_collection.find_one({"_id": ObjectId(channel_id)})
