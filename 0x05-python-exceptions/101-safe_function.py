#!/usr/bin/python3
import sys


# function htat executes a function safely
def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        return None

    return result
