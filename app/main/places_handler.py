#!/usr/bin/python3

import googlemaps
import os
import json
import requests


def test():
    key = get_key()
    gmaps = googlemaps.Client(key)

    place = gmaps.places('Orlando')

    get_place_location(place)

    return place


def get_key():
    with open(os.path.dirname(__file__)+'key.txt') as key:
        return key.readline()


def get_place_location(place):
    center = ''
    key = get_key()
    gmaps = googlemaps.Client(key)
    for key, value in place['results'][0].items():
        #print(type(value))
        if isinstance(value, dict):
            print(value)
            center = value['location']

    print(center)

    f = open('local_filename', 'wb')
    for chunk in gmaps.static_map(size=(400, 400), center=(center['lat'], center['lng']),
                                        zoom=15):
        if chunk:
            f.write(chunk)
        f.close()



if __name__ == '__main__':
    test()
