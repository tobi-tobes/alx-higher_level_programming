#!/usr/bin/python3
"""
Rectangle Class
This module defines a class Rectangle with given parameters
"""


class Rectangle:
    """Represents a rectangle with a width determined by user input"""
    def __init__(self, width=0, height=0):
        """Creates a new rectangle with the width and
        height coordinates given as an argument"""
        self.__width = self.is_valid_width(width)
        self.__height = self.is_valid_height(height)

    def __del__(self):
        """Deletes a rectangle"""
        print("Bye rectangle...")

    def is_valid_width(self, value):
        """Checks that initial width input is valid before creating instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            return (value)

    def is_valid_height(self, value):
        """Checks that initial height input is
valid before creating instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            return (value)

    @property
    def width(self):
        """Retrieves the value of the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Updates the width attribute with the value given as an argument
        after checking that the value fits specific parameters"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the value of the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Updates the height attribute with the value given as an argument
        after checking that the value fits specific parameters"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the current rectangle area based on the given dimensions"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the current rectangle perimeter
based on the given dimensions"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Determines what is printed out by print()"""
        output = ""
        if self.__width == 0 or self.__height == 0:
            return (output)
        width = self.__width
        height = self.__height
        for i in range(height):
            for j in range(width):
                output += "#"
            if i != height - 1:
                output += "\n"
        return (output)

    def __repr__(self):
        """Returns the Python code needed to reproduce the current instance"""
        return (f'Rectangle({self.__width}, {self.__height})')
