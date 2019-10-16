#!/usr/bin/python3
"""Function that return if the object is an instance"""


def is_kind_of_class(obj, a_class):
    """Function that return if the object is an instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
