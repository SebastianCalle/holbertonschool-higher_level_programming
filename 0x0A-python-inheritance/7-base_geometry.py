#!/usr/bin/python3

class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """area of base geomeru"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator of integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater that 0".format(name))
