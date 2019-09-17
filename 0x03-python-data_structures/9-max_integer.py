#!/usr/bin/python3
def max_integer(my_list=[]):
    a = [0]
    if my_list is None and len(my_list) == 0:
        return None
    else:
        for i in range(0, len(my_list)):
            if my_list[i] >= a[0]:
                a[0] = my_list[i]
        return a[0]
