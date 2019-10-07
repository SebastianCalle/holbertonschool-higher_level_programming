#!/usr/bin/python3
"""multiplicate two matrix"""


import numpy as np
"""
    Function that multiplicate whit numpy a matrix
"""


def lazy_matrix_mul(m_a, m_b):
    """function that return a matrix multiplicate"""
    return np.matmul(m_a, m_b)
