#!/usr/bin/python3
"""Function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file"""
    with open(filename, 'w', encoding='utf8') as f:
        a = f.write(str(text))
        return a
