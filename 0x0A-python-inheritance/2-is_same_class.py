#!/usr/bin/python3
"""
is_same_class Function
This module defines a function `def is_same_class(obj, a_class):`
that returns True if an object is exactly an instance of the
specified class, else False
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance
 of the specified class ; otherwise False."""
    return (type(obj) is a_class)
