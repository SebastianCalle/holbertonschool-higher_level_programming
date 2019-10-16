#!/usr/bin/python3


def read_file(filename=""):
    """Function that read a file"""
    with open(filename, 'r') as f:
        read_data = f.read()
        print(read_data, end="")
