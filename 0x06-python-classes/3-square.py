#!/usr/bin/python3
class Square:
    """Square object"""
    def __init__(self, size=0):
        """Inizializate class"""
        self.__size = size
        if type(self.__size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if self.__size < 0:
            print("size must be >= 0", end="")
            raise ValueError

    def area(self):
        """Calculate area of square"""
        return self.__size * self.__size
