#!/usr/bin/python3


# function that returns a set of all ellements present in only one set
def only_diff_elements(set_1, set_2):
    set_3 = set_1.symmetric_difference(set_2)
    return set_3
