#!/usr/bin/python3

import googlemaps
import os
import json
import requests


def get_key():
    with open(os.path.dirname(__file__) + '/key.txt') as key:
        return key.readline()


key = get_key()
gmaps = googlemaps.Client(key)


def test():

    place = gmaps.places('Orlando')

    get_place_location(place)

    return place


def get_place_location(place):
    center = ''
    key = get_key()
    gmaps = googlemaps.Client(key)
    for key, value in place['results'][0].items():
        # print(type(value))
        if isinstance(value, dict):
            print(value)
            center = value['location']

    print(center['lat'],center['lng'])

    f = open('../static/local_filename.PNG', 'wb')
    for chunk in gmaps.static_map(size=(400, 400), center=(str(center['lat']),str(center['lng'])), zoom=10):

        if chunk:
            f.write(chunk)
    f.close()


if __name__ == '__main__':
    test()
