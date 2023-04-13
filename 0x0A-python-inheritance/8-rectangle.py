#!/usr/bin/python3
"""
BaseGeometry Class
This module defines a class BaseGeometry and its subclass Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines a class Rectangle that is a subclass of BaseGeometry"""
    def __init__(self, width, height):
        """instantiates a Rectangle instance"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
