#!/usr/bin/python3
import os.path
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""Function that add item to a list"""


def add_item():
    """Function that add item to a list"""
    ar = len(argv)
    f = 'add_item.json'
    lo = []
    i = 1
    if os.path.isfile(f):
        lo = load_from_json_file(f)
        while i < ar:
            lo.append(argv[i])
            save_to_json_file(lo, f)
            i += 1
    else:
        open(f, 'w')
        save_to_json_file(lo, f)
        while i < ar:
            lo.append(argv[i])
            save_to_json_file(lo, f)
            i += 1


if __name__ == '__main__':
    add_item()
