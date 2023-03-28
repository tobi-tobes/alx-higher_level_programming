#!/usr/bin/python3
"""
Square Class

This module defines a class Square with given parameters
"""


class Square:
    """Represents a square with a size determined by user input"""
    def __init__(self, size):
        """Creates a new square with the size given as an argument
        after checking that the size fits specific parameters"""
        self.__size = size
