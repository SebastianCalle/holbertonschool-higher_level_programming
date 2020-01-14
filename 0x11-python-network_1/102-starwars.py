#!/usr/bin/python3
# Script that takes in a letter and sends a POST

import requests
import sys


if __name__ == "__main__":
    search = sys.argv[1]
    url = 'https://swapi.co/api/people/'
    r = requests.get(url, params={'search': search})
    data = r.json()
    result = r.json()['results']
    print("Number of results:", r.json()['count'])
    while data['next'] is not None:
        r = requests.get(data['next'])
        data = r.json()
        result += data['results']

    for name in result:
        print(name['name'])
        films = name.get('films')
        for film in films:
            r = requests.get(film)
            film = r.json()
            print("\t{}".format(film.get('title')))
