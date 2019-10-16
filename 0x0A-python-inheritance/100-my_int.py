#!/usr/bin/python3
"""Class MyInt"""


class MyInt(int):
    """class MyInt"""

    def __init__(self, value):
        """Initializate attributes"""
        self.__value = value

    def __eq__(self, other):
        """Method equal"""
        return self.__value != other

    def __ne__(self, other):
        """method not equal"""
        return self.__value == other
