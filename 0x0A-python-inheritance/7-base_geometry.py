#!/usr/bin/python3
"""
BaseGeometry Class
This module defines an empty class BaseGeometry
"""


class BaseGeometry:
    """defines an empty class BaseGeometry"""
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
