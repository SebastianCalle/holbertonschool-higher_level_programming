#!/usr/bin/python3
class Square:
    """Square object"""
    def __init__(self, size=0):
        """Inizializate class"""
        self.__size = size

    @property
    def size(self):
        """Return a atributte size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        return self.__size

    def area(self):
        """Calculate area of square"""
        return self.__size * self.__size

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.area() == other.area()

    def __lt__(self, other):
        """Override the default less than behavior"""
        return self.area() < other.area()

    def __ne__(self, other):
        """Override the default not equal behavior"""
        return self.area() != other.area()

    def __le__(self, other):
        """Override the default less or  equal behavior"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Override the default greater than behavior"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Override the default greater or equal behavior"""
        return self.area() >= other.area()
