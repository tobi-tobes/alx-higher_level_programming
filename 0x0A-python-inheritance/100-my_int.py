#!/usr/bin/python3
"""
MyInt Class
This module defines a class MyInt that is
a subclass of int
"""


class MyInt(int):
    """defines a class MyInt that inherits from int"""
    def __new__(cls, value):
        """initializes an instance of MyInt"""
        if type(value) is not int:
            raise TypeError("Instance of MyInt must be an integer")
        return super().__new__(cls, value)

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """Enables equality operator for the MyInt class"""
        return self.real != other.real

    def __ne__(self, other):
        """Enables not equal operator for the MyInt class"""
        return self.real == other.real
