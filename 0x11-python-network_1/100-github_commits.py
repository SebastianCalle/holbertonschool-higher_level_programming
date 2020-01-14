#!/usr/bin/python3
# Script that takes in a letter and sends a POST

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)
    results = r.json()
    i = 0
    for obj in results:
        author = obj.get('commit').get('author').get('name')
        print('{}: {}'.format(obj.get('sha'), author))
        if i == 9:
            break
        i += 1
