import googlemaps
import os
import json


def test():
    key = get_key()
    gmaps = googlemaps.Client(key)

    place = gmaps.places('France')

    get_place_location(place)

    return place


def get_key():
    with open(os.path.dirname(__file__)+'key.txt') as key:
        return key.readline()


def get_place_location(place):
    for key, value in place.items():
            print(key)


if __name__ == '__main__':
    test()
