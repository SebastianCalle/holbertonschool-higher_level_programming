#!/usr/bin/python3
"""Class Square that inherits fromt Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle
"""Import class Rectangle"""


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """Initializate attributes"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """return string"""
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Return area of Square"""
        return self.__size ** 2
