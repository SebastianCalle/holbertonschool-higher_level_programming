#!/usr/bin/python3


# Function that prints x elements of a list
def safe_print_list(my_list=[], x=0):
    i = 0
    j = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            j += 1
            i += 1
        except IndexError:
            i += 1
    print("")
    return j
