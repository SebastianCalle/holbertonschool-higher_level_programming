#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """area of base BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator of integer"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater that 0".format(name))
