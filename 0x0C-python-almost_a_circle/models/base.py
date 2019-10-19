#!/usr/bin/python3

import json
"""Module Python"""

"""Base of the modules"""


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializate attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON representation"""
        if not isinstance(
                list_dictionaries,
                list) and list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            string = json.dumps(list_dictionaries)
            return string
