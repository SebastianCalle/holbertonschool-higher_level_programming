#!/usr/bin/python3


# function that adds all unique integers in a list
def uniq_add(my_list=[]):
    sum_total = 0
    for i in list(set(my_list)):
        sum_total += i
    return sum_total
