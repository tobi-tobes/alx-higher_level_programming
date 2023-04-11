#!/usr/bin/python3
"""
Lookup Function
This module defines a function `def lookup(obj): that
returns the list of available attributes and methods of
an object.
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
