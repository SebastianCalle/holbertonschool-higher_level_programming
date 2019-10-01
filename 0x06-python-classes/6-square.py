#!/usr/bin/python3
class Square:
    """Square object"""
    def __init__(self, size=0, position=(0, 0)):
        """Inizializate class"""
        self.size = size
        self.position = position

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

    def my_print(self):
        """Print a square whit character #"""
        pos = self.__position[1]
        if pos > 0:
            pos = 0
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if j == pos:
                    print(" " * self.__position[0], end="")
                print("#", end="")
            print("")

    @property
    def position(self):
        """Return the private value"""
        return self.__position

    @position.setter
    def position(self, value):
        """Print space in position"""
        for i in range(0, len(value)):
            if (i >= 2 or type(value[i]) is not int or
                    value[i] < 0 or type(value) is not tuple):
                raise TypeError("position must be a tuple"
                                " of 2 positive integers")
        self.__position = value
        return self.__position
