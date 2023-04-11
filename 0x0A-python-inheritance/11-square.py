#!/usr/bin/python3
"""
BaseGeometry Class
This module defines a class BaseGeometry and its
 subclasses Rectangle and Square
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

    def area(self):
        """computes the area of the rectangle"""
        return(self.__width * self.__height)

    def __str__(self):
        """returns the string representation of a Rectangle object"""
        return(f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """defines a class Square that is a subclass of Rectangle"""
    def __init__(self, size):
        """instantiates a Square instance"""
        super().integer_validator("width", size)
        super().integer_validator("height", size)
        self.__width = size
        self.__height = size

    def area(self):
        """computes the area of the Square"""
        return(self.__width * self.__height)

    def __str__(self):
        """returns the string representation of a Square object"""
        return (f"[Square] {self.__width}/{self.__height}")
