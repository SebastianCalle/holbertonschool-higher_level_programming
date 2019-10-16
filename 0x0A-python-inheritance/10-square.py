#!/usr/bin/python3
"""Class Square that inhertis from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle
"""Import class Rectangle"""


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """Initializate attributes"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area of square"""
        return self.__size ** 2
