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

    def to_json(self):
        """Method to json"""
        return self.__dict__
