#!/usr/bin/python3


# function that print the first x elements of a list and only integers
def safe_print_list_integers(my_list=[], x=0):
    i, j = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            j += 1
        except (ValueError, TypeError):
            i += 1
            continue
    print("")
    return j
