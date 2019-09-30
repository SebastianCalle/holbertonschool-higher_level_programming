#!/usr/bin/python3


# function that divides element by element 2 lists
def list_division(my_list_1, my_list_2, list_length):
    length = []
    for i in range(0, list_length):
        try:
            length.append(my_list_1[i] / my_list_2[i])
        except (ZeroDivisionError):
            print("division by 0")
            length.append(0)
        except TypeError:
            print("wrong type")
            length.append(0)
        except IndexError:
            print("out of range")
            length.append(0)

    return length

