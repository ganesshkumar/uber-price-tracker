import os
from pymongo import MongoClient

client = MongoClient(os.environ['DATABASE_URI'])

db = client['uber-tracking-data']
tracks = db['price_tracks']

def add_track(data):
    global tracks
    tracks.insert_one(data)
