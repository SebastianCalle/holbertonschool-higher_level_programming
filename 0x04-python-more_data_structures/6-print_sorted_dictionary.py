#!/usr/bin/python3


# function that prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print('{}: {}'.format(i, a_dictionary[i]))
