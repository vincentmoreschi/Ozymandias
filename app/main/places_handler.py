#!/usr/bin/python3
from .. models import MapData
import googlemaps
import os
import json
import requests
import uuid
from .. import db

def get_key():
    with open(os.path.dirname(__file__) + '/key.txt') as key:
        return key.readline()


key = get_key()
gmaps = googlemaps.Client(key)


def test():

    place = gmaps.places('Orlando')

    get_place_location(place)

    return place


def get_place_location(query):
    uuidString = uuid.uuid4()

    photostring = uuidString
    key = get_key()
    gmaps = googlemaps.Client(key)
    place = gmaps.places(query)
    center = ''

    for key, value in place['results'][0].items():
        # print(type(value))
        if isinstance(value, dict):
            print(value)
            center = value['location']

    print(center['lat'], center['lng'])
    print(str(photostring))
    f = open('app/static/' + str(photostring)+ ".png", 'wb')
    map = gmaps.static_map(size=(400, 400), center=(str(center['lat']),str(center['lng'])), zoom=10)
    db.session.add(MapData(uuid=str(uuidString)))
    #db.session.add(map)
    db.session.commit()
    for chunk in map:

        if chunk:

            f.write(chunk)
    f.close()

    return str(photostring)+ ".png"

if __name__ == '__main__':
    test()
