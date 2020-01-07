#!/usr/bin/python3
# function that finds a peak in a list of unsorted integers
def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers
    """
    if list_of_integers:
        if len(list_of_integers) == 1:
            return list_of_integers[0]
        for i in range(1, len(list_of_integers)):
            if list_of_integers[i-1] > list_of_integers[i] and i > 0:
                aux = list_of_integers[i-1]
            else:
                aux = list_of_integers[i]
        return aux
    else:
        return None
