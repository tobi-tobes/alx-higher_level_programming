#!/usr/bin/python3
"""
Square Class
This module defines a class Square with given parameters
"""


class Square:
    """Represents a square with a size determined by user input"""
    def __init__(self, size=0, position=(0, 0)):
        """Creates a new square with the size and
        positional coordinates given as an argument"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves the value of the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Updates the position attribute with the value given as an argument
        after checking that the value fits specific parameters"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area based on the given dimensions"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square of given dimensions and
position with the character # to stdout"""
        if self.__size == 0:
            print()
        else:
            x = self.__position[0]
            y = self.__position[1]
            for i in range(y):
                print()
            for i in range(self.__size):
                print(" " * x, "#" * self.__size)

    def __str__(self):
        """Determines what is printed out by print()"""
        output = ""
        if self.__size == 0:
            return (output)
        else:
            x = self.__position[0]
            y = self.__position[1]
            for i in range(y):
                output += "\n"
            for i in range(self.__size):
                for k in range(x):
                    output += " "
                for j in range(self.__size):
                    output += "#"
                if i < self.__size - 1:
                    output += "\n"
        return (output)
