#!/usr/bin/python3
# Script that takes in a URL and an email, sends a POST request

import urllib.request
import urllib.parse
import sys


url = sys.argv[1]
email = sys.argv[2]
values = {'email': email}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    page = response.read()
    print(page)
