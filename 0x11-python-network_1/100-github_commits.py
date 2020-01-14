#!/usr/bin/python3
# Script that takes in a letter and sends a POST

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)
    result = r.json()
    for obj in result:
        author = obj.get('commit').get('author').get('name')
        print('{}: {}'.format(obj.get('sha'), author))
