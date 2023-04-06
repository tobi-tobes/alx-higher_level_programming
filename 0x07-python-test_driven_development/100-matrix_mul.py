#!/usr/bin/python3
"""
matrix_mul module
This module contains the function matrix_mul,
which multuplies two matrices together
"""


def matrix_mul(m_a=[[1]], m_b=[[1]]):
    """Returns a new matrix that is the product of the input matrices"""
    if m_a is None:
        raise ValueError("m_a must be a valid argument")
    elif m_b is None:
        raise ValueError("m_b must be a valid argument")
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")
    elif len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    elif type(m_a[0]) is not list:
        raise TypeError("m_a must be a list of lists")
    elif type(m_b[0]) is not list:
        raise TypeError("m_b must be a list of lists")
    compare_a = len(m_a[0])
    compare_b = len(m_b[0])
    if compare_a == 0:
        raise ValueError("m_a can't be empty")
    elif compare_b == 0:
        raise ValueError("m_b can't be empty")
    for i in range(len(m_a)):
        if type(m_a[i]) is not list:
            raise TypeError("m_a must be a list of lists")
        for j in range(len(m_a[i])):
            if type(m_a[i][j]) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        if len(m_a[i]) != compare_a:
            raise TypeError("each row of m_a must be of the same size")
    for i in range(len(m_b)):
        if type(m_b[i]) is not list:
            raise TypeError("m_b must be a list of lists")
        for j in range(len(m_b[i])):
            if type(m_b[i][j]) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        if len(m_b[i]) != compare_b:
            raise TypeError("each row of m_b must be of the same size")
    rows = len(m_a)
    cols = len(m_b[0])
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix_prod = []
    for i in range(rows):
        matrix_prod_row = []
        for j in range(cols):
            prod = 0
            for k in range(len(m_a[i])):
                mul_1 = m_a[i][k]
                mul_2 = m_b[k][j]
                prod += (mul_1 * mul_2) if type((mul_1 * mul_2))\
                    is int else round((mul_1 * mul_2), 2)
            matrix_prod_row.append(prod)
        matrix_prod.append(matrix_prod_row)
    return (matrix_prod)
