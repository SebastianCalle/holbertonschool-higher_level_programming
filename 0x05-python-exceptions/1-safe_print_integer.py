#!/usr/bin/python3


# function that prints an integer
def safe_print_integer(value):
    if not value:
        return False
    try:
        print("{:d}".format(value))
    except:
        return False

    return True
