#!/usr/bin/python3
import sys


# function that prints an integer
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        sys.stderr.write("Exception:" + str(err) + "\n")
        return False
    return True
