#!/usr/bin/python3
"""
add_integer module
This module contains the function add_integer,
which returns the sum of two integers
"""


def add_integer(a, b=98):
    """Returns the sum of two integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    num1 = int(a)
    num2 = int(b)
    return (num1 + num2)
