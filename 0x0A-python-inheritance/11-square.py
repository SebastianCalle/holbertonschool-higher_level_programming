#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle
"""Import class Rectangle"""

class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
