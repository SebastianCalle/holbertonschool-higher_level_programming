#!/usr/bin/python3

def add_attribute(obj, name, value):
    """adds new attribute"""
    if  hasattr(obj, '__dict__'):
        raise Exception("can't add new attribute")
    else:
        setattr(obj, name, value)
