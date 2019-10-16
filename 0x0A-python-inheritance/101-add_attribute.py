#!/usr/bin/python3
"""Add new attribute"""


def add_attribute(obj, name, value):
    """adds new attribute"""
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
