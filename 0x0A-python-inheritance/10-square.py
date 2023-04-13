#!/usr/bin/python3
"""
BaseGeometry Class
This module defines a class BaseGeometry and its
 subclasses Rectangle and Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a class Square that is a subclass of Rectangle"""
    def __init__(self, size):
        """instantiates a Square instance"""
        super().integer_validator("size", size)
        super().integer_validator("size", size)
        self.__width = size
        self.__height = size

    def area(self):
        """computes the area of the Square"""
        return (super().area())

    def __str__(self):
        """returns the string representation of a Square object"""
        return(super().__str__())
