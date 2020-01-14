#!/usr/bin/python3
# Script that takes in a letter and sends a POST

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}
    r = requests.post(url, data=payload)
    if type(r.json()) != dict:
        print('No a valid JSON')
    elif r.json().get('id') is None:
        print('No result')
    else:
        print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
