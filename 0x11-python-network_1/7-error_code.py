#!/usr/bin/python3
# Script that takes in a URL, sends a request

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code:", r.status_code) 
    else:
        print(r.text)
