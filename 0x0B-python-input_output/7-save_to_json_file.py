#!/usr/bin/python3
import json
"""Function that writes an Object to a text file """


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
