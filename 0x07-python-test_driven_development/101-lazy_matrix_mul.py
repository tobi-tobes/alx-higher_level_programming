#!/usr/bin/python3
"""
lazy_matrix_mul module
This module contains the function lazy_matrix_mul,
which multuplies two matrices together using numpy
"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """Returns a new matrix that is the product of the input matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a matrix")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a matrix")
    elif len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("your matrix can't be empty")
    elif type(m_a[0]) is not list:
        raise TypeError("m_a must be a matrix")
    elif type(m_b[0]) is not list:
        raise TypeError("m_b must be a matrix")
    compare_a = len(m_a[0])
    compare_b = len(m_b[0])
    if compare_a == 0 or compare_b == 0:
        raise ValueError("your matrix can't be empty")
    for i in range(1, len(m_a)):
        if type(m_a[i]) is not list:
            raise TypeError("m_a must be a matrix")
        elif len(m_a[i]) != compare_a:
            raise TypeError("each row of m_a must be the same length")
        for j in range(len(m_a[i])):
            if type(m_a[i][j]) not in [int, float]:
                raise TypeError("m_a must contain only integers or floats")
    for i in range(1, len(m_b)):
        if type(m_b[i]) is not list:
            raise TypeError("m_b must be a matrix")
        elif len(m_b[i]) != compare_b:
            raise TypeError("each row of m_b must be the same length")
        for j in range(len(m_b[i])):
            if type(m_b[i][j]) not in [int, float]:
                raise TypeError("m_b must contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("your matrices can't be multiplied")
    return (numpy.dot(m_a, m_b))
