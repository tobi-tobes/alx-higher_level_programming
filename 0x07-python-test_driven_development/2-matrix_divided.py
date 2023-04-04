#!/usr/bin/python3
"""
matrix_divided module
This module contains the function matrix_divided,
 which divides the elements of a matrix by div
"""


def matrix_divided(matrix, div):
    """Returns a new matrix containing the quotients
 of division of the elements of matrix with div"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    elif len(matrix) == 0:
        raise ValueError("your matrix can't be empty")
    elif type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    compare = len(matrix[0])
    if compare == 0:
        raise ValueError("your matrix can't be empty")
    for i in range(1, len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        elif len(matrix[i]) != compare:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    matrix_quot = []
    for i in range(len(matrix)):
        matrix_quot_row = []
        for j in range(len(matrix[i])):
            matrix_quot_row.append(round((matrix[i][j] / div), 2))
        matrix_quot.append(matrix_quot_row)
    return (matrix_quot)
