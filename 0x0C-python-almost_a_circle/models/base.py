#!/usr/bin/python3

import json
"""Module Python"""
"""Base of the modules"""


class Base:
    """Class Base"""

    __nb_objects = 0

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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation"""
        if list_objs:
            list_d = []
            for obj in list_objs:
                if isinstance(obj, cls):
                    with open(cls.__name__ + '.json', 'w') as f:
                            dict1 = obj.to_dictionary()
                            list_d.append(dict1)
                            data = cls.to_json_string(list_d)
                            f.write(data)
        else:
                with open(cls.__name__ + '.json', 'w') as f:
                        data = cls.to_json_string(list_objs)
                        f.write(data)


    def __init__(self, id=None):
        """Initializate attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

