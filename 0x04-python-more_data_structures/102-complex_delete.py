#!/usr/bin/python3


# function that deletes keys with a specific value in a dictionary
def complex_delete(a_dictionary, value):
    list_del = []
    for key, val in a_dictionary.items():
        if val == value:
            list_del.append(key)
    for key in list_del:
        if key in a_dictionary:
            del a_dictionary[key]
    return a_dictionary
