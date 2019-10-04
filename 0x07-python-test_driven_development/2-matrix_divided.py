#!/usr/bin/python3
"""
    function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Function matix divided"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [i[:] for i in matrix]
    rows = len(matrix[0])
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if len(matrix[i]) != rows:
                raise TypeError("Each row of the matrix must"
                                " have the same size")
            if type(matrix[i]) is not list:
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
            if (type(matrix[i][j]) is not int and
                    type(matrix[i][j]) is not float):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
            new_matrix[i][j] = round((matrix[i][j] / div), 2)
    return new_matrix
