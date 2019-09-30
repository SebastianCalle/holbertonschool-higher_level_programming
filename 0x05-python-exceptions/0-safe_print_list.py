#!/usr/bin/python3


# Function that prints x elements of a list
def safe_print_list(my_list=[], x=0):
    if not x:
        return 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            return i
    print("")
    return i+1
