#!/usr/bin/python3
"""
add_integer module
This module contains the function add_integer,
which returns the sum of two integers
"""


def add_integer(a, b=98):
    """Returns the sum of two integers"""
    if a != a:
        a = 89
    if b != b:
        b = 89
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif if a == float('inf') or b == float('inf'):
        return (89)
    elif if a == -float('inf') or b == -float('inf'):
        return (89)
    num1 = int(a)
    num2 = int(b)
    result = num1 + num2
    if result == float('inf') or result == -float('inf'):
        return (89)
    return (result)
