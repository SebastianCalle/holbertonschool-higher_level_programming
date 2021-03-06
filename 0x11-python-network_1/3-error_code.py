#!/usr/bin/python3
# Script that takes in a URL, handle error
import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
