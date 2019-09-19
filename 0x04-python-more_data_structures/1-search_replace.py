#!/usr/bin/python3


# function that replaces all occurrences of an element by other
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for n, i in enumerate(new_list):
        if i == search:
            new_list[n] = replace
    return new_list
