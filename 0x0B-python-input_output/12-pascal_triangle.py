#!/usr/bin/python3
"""
pascal_triangle module
This module contains the function pascal_triangle,
returns a list of lists of integers representing the
Pascal's triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the
Pascal's triangle of n"""
    if n <= 0:
        return []
    pascal_tri = []
    for i in range(n):
        sub_list = []
        if i == 0:
            sub_list.append(1)
        elif i == 1:
            sub_list.append(1)
            sub_list.append(1)
        else:
            for j in range(len(pascal_tri[i - 1])):
                if j == 0:
                    sub_list.append(pascal_tri[i - 1][j] + 0)
                elif j == len(pascal_tri[i - 1]) - 1:
                    sub_list.append(pascal_tri[i - 1][j] +
                                    (pascal_tri[i - 1][j - 1]))
                    sub_list.append(pascal_tri[i - 1][j] + 0)
                else:
                    sub_list.append(pascal_tri[i - 1][j] +
                                    (pascal_tri[i - 1][j - 1]))
        pascal_tri.append(sub_list)
    return pascal_tri
