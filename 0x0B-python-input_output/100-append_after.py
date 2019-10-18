#!/usr/bin/python3
"""Function that add new lines to file"""


def append_after(filename="", search_string="", new_string=""):
    """Function that add new lines to file"""
    with open(filename, 'r+') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
