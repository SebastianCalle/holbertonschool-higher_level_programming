#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None and len(my_list) <= 0:
        return None
    else:
        a = my_list[0]
        for i in range(0, len(my_list)):
            if my_list[i] >= a:
                a = my_list[i]
        return a
