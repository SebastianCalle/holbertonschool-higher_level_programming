#!/usr/bin/python3
"""Class Studend
    attributes: firts_name, second_name, age
"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializate attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to json"""
        dict1 = self.__dict__
        dict2 = {}
        if attrs:
            for key in attrs:
                if key in dict1:
                    dict2[key] = dict1.get(key)
            return dict2
        else:
            return dict1
