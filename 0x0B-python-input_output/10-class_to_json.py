#!/usr/bin/python3
import json
"""Function that returns the dictionary description"""


def class_to_jason(obj):
    """Function that returns the dictionary description"""
    return json.dumps(obj.__dict__)
