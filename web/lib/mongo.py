from flask import current_app
from flask.ext.pymongo import PyMongo

MONGO_CONNECTION = None

def get_db():
    global MONGO_CONNECTION
    if not MONGO_CONNECTION:
        MONGO_CONNECTION = PyMongo(current_app).db

    return MONGO_CONNECTION
