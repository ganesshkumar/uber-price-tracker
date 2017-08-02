import os
from pymongo import MongoClient

def add_track(data):
    client = MongoClient(os.environ['DATABASE_URI'])

    db = client['uber-tracking-data']
    tracks = db['price_tracks']

    tracks.insert_one(data)
    client.close()
