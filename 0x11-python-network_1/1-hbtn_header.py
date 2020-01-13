#!/usr/bin/python3
# Script that takes in a URL, sends a request to the URL

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = url
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])
