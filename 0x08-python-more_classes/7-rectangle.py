#!/usr/bin/python3
class Rectangle:
    """class Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """str method"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = []
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rec.append(str(self.print_symbol))
            rec.append("\n")

        rec.pop()

        return "".join(rec)

    def __repr__(self):
        """repr method"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

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

    def area(self):
        """Calculate area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter of Rectangle"""
        perimeter = 2 * (self.__height + self.__width)
        return perimeter

    def __del__(self):
        """Destructure method"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
