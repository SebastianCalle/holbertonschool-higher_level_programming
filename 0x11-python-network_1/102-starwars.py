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
        for i in range(len(name['films'])):
            numb = name['films'][i][-2:-1]
            url = 'https://swapi.co/api/films/{}'.format(numb)
            r = requests.get(url)
            print('\t', r.json()['title'])
