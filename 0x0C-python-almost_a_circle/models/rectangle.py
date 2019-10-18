#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return width private"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width attribute"""
        self.__width = value

    @property
    def height(self):
        """Return height private"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height attribute"""
        self.__height = value

    @property
    def x(self):
        """Return x private"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x attribute"""
        self.__x = value

    @property
    def y(self):
        """Return y private"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y attribute"""
        self.__y = value
