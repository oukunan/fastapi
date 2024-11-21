from database import channels_collection
from bson.objectid import ObjectId


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


def update_channel(id, data):
    channels_collection.update_one({"_id": ObjectId(id)}, {"$set": data})


def get_channel_by_id(id):
    if not ObjectId.is_valid(id):
        return None
        
    return channels_collection.find_one({"_id": ObjectId(id)})
