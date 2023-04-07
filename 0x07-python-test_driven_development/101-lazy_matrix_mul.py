#!/usr/bin/python3
"""
lazy_matrix_mul module
This module contains the function lazy_matrix_mul,
which multuplies two matrices together using numpy
"""


import numpy


def lazy_matrix_mul(m_a=[[1]], m_b=[[1]]):
    """Returns a new matrix that is the product of the input matrices"""
    if type(m_a) is not list or type(m_b) is not list:
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    h_a = len(m_a)
    w_a = len(m_a[0]) if h_a != 0 else 0
    h_b = len(m_b)
    w_b = len(m_b[0]) if h_b != 0 else 0
    if h_a == 0 or w_a == 0 or h_b == 0 or w_b == 0:
        raise ValueError("shapes ({:d},{:d}) and ({:d},{:d}) not aligned: {:d}\
 (dim 1) != {:d} (dim 0)".format(h_a, w_a, h_b, w_b, w_a, h_b))
    for i in range(len(m_a)):
        if type(m_a[i]) is not list:
            raise TypeError("invalid data type for einsum")
        elif len(m_a[i]) != w_a:
            raise ValueError("setting an array element with a sequence.")
        for j in range(len(m_a[i])):
            if type(m_a[i][j]) not in [int, float]:
                raise TypeError("invalid data type for einsum")
    for i in range(len(m_b)):
        if type(m_b[i]) is not list:
            raise TypeError("invalid data type for einsum")
        elif len(m_b[i]) != w_b:
            raise ValueError("setting an array element with a sequence.")
        for j in range(len(m_b[i])):
            if type(m_b[i][j]) not in [int, float]:
                raise TypeError("invalid data type for einsum")
    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes ({:d},{:d}) and ({:d},{:d}) not aligned: {:d}\
 (dim 1) != {:d} (dim 0)".format(h_a, w_a, h_b, w_b, w_a, h_b))
    return (numpy.dot(m_a, m_b))
