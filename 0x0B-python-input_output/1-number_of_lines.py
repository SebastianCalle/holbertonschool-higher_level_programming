#!/usr/bin/python3
"""FUnction that return the number of lines of a text file"""


def number_of_lines(filename=""):
    """FUnction that return the number of lines of a text file"""
    i = 0
    with open(filename, 'r') as f:
        for line in f:
            i += 1

    return i
