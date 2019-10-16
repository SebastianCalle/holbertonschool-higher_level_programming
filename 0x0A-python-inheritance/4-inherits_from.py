#!/usr/bin/python3
"""Function that reurn if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """Function that reurn if the object is an instance of a class"""
    if isinstance(obj, a_class):
        return False
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False
