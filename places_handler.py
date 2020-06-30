import googlemaps
import os
import json


def test():
    key = get_key()
    gmaps = googlemaps.Client(key)

    place = gmaps.places('France')

    return place


def get_key():
    with open(os.path.dirname(__file__)+'/key.txt') as key:
        return key.readline()


def place_parser(place):
    parse = json.load(place)


if __name__ == '__main__':
    print(test())
