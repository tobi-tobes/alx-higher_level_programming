#!/usr/bin/python3
import math


class MagicClass:
    """ creates a circle"""

    def __init__(self, radius=0):
        """ initializes an object """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ calculates the  area """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ calculates the circumference """
        return ((2 * math.pi) * self.__radius)
