#!/usr/bin/python3
# Script that fetches of url

import urllib.request
import urllib.parse


req = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(req) as response:
    page = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(page)))
    print('\t- content: {}'.format(page))
    print('\t- utf8 content: {}'.format(page.decode('utf8')))
