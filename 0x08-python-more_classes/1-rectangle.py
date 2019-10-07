#!/usr/bin/python3
class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """Return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    @property
    def width(self):
        """return the whidth"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
