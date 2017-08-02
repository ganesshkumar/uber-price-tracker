import os
from datetime import datetime
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

from locations import coordinates

session = Session(server_token=os.environ['UBER_SERVER_TOKEN'])
client = UberRidesClient(session)

def __get_estimate(source, destination):
    prices = {}

    response = client.get_price_estimates(
        start_latitude=source['lat'], start_longitude=source['lng'],
        end_latitude=destination['lat'], end_longitude=destination['lng']
    )

    estimates = response.json.get('prices')
    for estimate in estimates:
        prices[estimate['display_name']] = {
            'low': estimate['low_estimate'],
            'high': estimate['high_estimate'],
            'distance': estimate['distance'],
            'duration': estimate['duration'],
            'surge_multiplier': estimate['surge_multiplier'] if 'surge_multiplier' in estimate else 1
        }

    return prices

def __get_store_data(utctime, estimate, source, destination):
    return {
        'estimates': estimate,
        'source': source,
        'destination': destination,
        'year': utctime.year,
        'month': utctime.month,
        'day': utctime.day,
        'day_of_week': utctime.strftime('%a'),
        'hour': utctime.hour,
        'minute': utctime.minute,
        'second': utctime.second
    }

def get_tracking_data(sourceName, destinationName):
    return __get_store_data(datetime.utcnow(), __get_estimate(coordinates[sourceName], coordinates[destinationName]), sourceName, destinationName)
