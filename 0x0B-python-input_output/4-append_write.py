#!/usr/bin/python3
"""Function that appends a string at the end of a text"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text"""
    with open(filename, 'a') as f:
        a = f.write(str(text))
        return a
