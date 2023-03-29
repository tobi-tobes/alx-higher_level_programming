#!/usr/bin/python3
"""
Square Class
This module defines a class Square with given parameters
"""


class Square:
    """Represents a square with a size determined by user input"""
    def __init__(self, size=0):
        """Creates a new square with the size given as an argument"""
        self.__size = size

    @property
    def size(self):
        """Retrieves the value of the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Creates a new square with the size given as an argument
        after checking that the size fits specific parameters"""
        if type(value) is not int or type(value) is not float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area based on the given dimensions"""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Enables equality operator for the Square class"""
        return (self.__size == other.__size)

    def __lt__(self, other):
        """Enables lesser than operator for the Square class"""
        return (self.__size < other.__size)

    def __le__(self, other):
        """Enables lesser than or equal to operator for the Square class"""
        return (self.__size <= other.__size)

    def __ne__(self, other):
        """Enables not equal operator for the Square class"""
        return (self.__size != other.__size)

    def __gt__(self, other):
        """Enables greater than operator for the Square class"""
        return (self.__size > other.__size)

    def __ge__(self, other):
        """Enables greater than or equal to operator for the Square class"""
        return (self.__size >= other.__size)
