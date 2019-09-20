#!/usr/bin/python3


# function that returns the wighted avarefe of all integers tuple
def weight_average(my_list=[]):
    if my_list is not None and len(my_list) > 0:
        new_list = []
        for i in range(0, len(my_list)):
            new_list += list(my_list[i])
        suma = 0
        div = 0
        i = 0
        while i < len(new_list):
            suma += new_list[i] * new_list[i+1]
            div += new_list[i+1]
            i += 2
        return suma / div
    return 0
