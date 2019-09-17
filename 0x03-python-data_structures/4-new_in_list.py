#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None and len(my_list) > 0:
        new_list = my_list[:]
        if idx > len(my_list) or idx < 0:
            return new_list
        new_list[idx] = element
        return new_list
