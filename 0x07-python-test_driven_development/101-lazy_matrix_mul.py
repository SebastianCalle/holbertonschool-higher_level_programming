#!/usr/bin/python3
import numpy as np
"""
    Function that multiplicate whit numpy a matrix
"""

def lazy_matrix_mul(m_a, m_b):
    """function that return a matrix multiplicate"""
    a = np.array(m_a)
    b = np.array(m_b)
    
    c = a @ b
    return c
