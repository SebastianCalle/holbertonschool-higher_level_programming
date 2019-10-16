#!/usr/bin/python3
"""Funtion that read n lines of a text file"""


def read_lines(filename="", nb_lines=0):
    """Funtion that read n lines of a text file"""
    i = 0
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            data = f.read()
            print(data, end="")
        else:
            for i in range(0, nb_lines):
                data = f.readline()
                print(data, end="")
