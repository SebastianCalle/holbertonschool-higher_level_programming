#!/usr/bin/python3
# Script that takes in a URL, sends a request to the URL

import urllib.request
import sys


url = sys.argv[1]
req = url
with urllib.request.urlopen(req) as response:
    print(response.headers.get('X-Request-Id'))
