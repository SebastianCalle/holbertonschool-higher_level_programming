#!/usr/bin/python3

# function that adds all unique integers in a list
def uniq_add(my_list=[]):
    my_list.sort()
    sum_total = 0
    for n, i in enumerate(my_list):
        if my_list[n-1] != i:
            sum_total += i
    return sum_total
