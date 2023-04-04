#!/usr/bin/python3
"""
print_square module
This module contains the function print_square,
 which prints a square with the character `#`.
"""


def print_square(size):
    """Prints a square with the given dimension size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
