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
        """Updates the size attribute with the value given as an argument
        after checking that the value fits specific parameters"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area based on the given dimensions"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square of given dimensions
with the character # to stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
