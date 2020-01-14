#!/usr/bin/python3
# Script that takes in a letter and sends a POST

import requests
import sys


if __name__ == "__main__":
    search = sys.argv[1]
    url = 'https://swapi.co/api/people/'
    r = requests.get(url, params={'search': search})
    result = r.json()['results']
    print("Number of results:", r.json()['count'])
    for name in result:
        print(name['name'])
