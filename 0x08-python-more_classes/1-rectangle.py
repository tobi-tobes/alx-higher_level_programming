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
