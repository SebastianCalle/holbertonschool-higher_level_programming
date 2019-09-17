#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    print(len(tuple_b))
    if len(tuple_b) == 1:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
        return tuple_c
    elif len(tuple_b) == 0:
        tuple_c = (tuple_a[0] + 0, tuple_a[1] + 0)
        return tuple_c
    if len(tuple_a) == 1:
        tuple_c = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
        return tuple_c
    elif len(tuple_a) == 0:
        tuple_c = (0 + tuple_b[0], 0 + tuple_b[1])
        return tuple_c
    if tuple_a is not None or tuple_b is not None:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_c
