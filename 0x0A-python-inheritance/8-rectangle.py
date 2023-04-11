#!/usr/bin/python3
"""
BaseGeometry Class
This module defines a class BaseGeometry and its subclass Rectangle
"""


class BaseGeometry(object):
    """defines a class BaseGeometry"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(locals()['name']))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(locals()
                                                                ['name']))


class Rectangle(BaseGeometry):
    """defines a class Rectangle that is a subclass of BaseGeometry"""
    def __init__(self, width, height):
        """instantiates a Rectangle instance"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
