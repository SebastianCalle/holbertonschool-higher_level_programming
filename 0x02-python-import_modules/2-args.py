#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    print('0 arguments.')
else:
    print(len(argv)-1, 'arguments:')
    i = 1
    while i < len(argv):
        print('{:d}:'.format(i), argv[i])
        i += 1
