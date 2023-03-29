#!/usr/bin/python3
import math


class MagicClass:
    """Represents a circle"""
    def __init__(self, radius=0):
        """Creates an instance of MagicClass"""
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area based on the given radius"""
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        """Calculates the circumference based on the given radius"""
        return (self.__radius * math.pi * 2)
