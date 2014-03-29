from pymongo import MongoClient

from config import Config

client = MongoClient(Config.get("MONGO", "MONGO_URI"))

def get_collection(collection_name):
    return _get_db()[collection_name]

def _get_db():
    return client['wattaco']
