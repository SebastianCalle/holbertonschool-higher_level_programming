#!/usr/bin/python3


# function that returns a new dictionary whit all values mul by 2
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for n, i in new_dic.items():
        new_dic[n] = i * 2
    return new_dic
