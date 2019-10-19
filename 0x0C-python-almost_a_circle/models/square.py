#!/usr/bin/python3

from .rectangle import Rectangle
"""import models"""

class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """Return string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """Return private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter size attribute"""
        self.width = value
        self.height = value
