#!/usr/bin/python3
"""Class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Import class BaseGeometry"""


class Rectangle(BaseGeometry):
    """ class Rectangle"""

    def __init__(self, width, height):
        """Initializate attributes"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
