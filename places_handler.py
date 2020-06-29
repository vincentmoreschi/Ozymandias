import googlemaps
from datetime import datetime
import os

def test():
    key = get_key()
    gmaps = googlemaps.Client(key)

    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                         "Parramatta, NSW",
                                         mode="transit",
                                         departure_time=now)

    return directions_result;

def get_key():
    with open(os.path.dirname(__file__)+'/key.txt') as key:
        return key.readline()
if __name__ == '__main__':
    print(test())
