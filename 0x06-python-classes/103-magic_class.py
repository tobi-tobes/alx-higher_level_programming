#!/usr/bin/python3
import math


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius=0):
        """Creates an instance of MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates the area based on the given radius"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Calculates the circumference based on the given radius"""
        return ((2 * math.pi) * self.__radius)
