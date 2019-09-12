#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        print('0 arguments.')
    else:
        if len(argv) == 2:
            print(len(argv)-1, 'argument:')
        else:
            print(len(argv)-1, 'arguments:')
        i = 1
        while i < len(argv):
            print('{:d}:'.format(i), argv[i])
            i += 1
