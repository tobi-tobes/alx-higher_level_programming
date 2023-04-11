#!/usr/bin/python3
"""
is_kind_of_class Function
This module defines a function `def is_kind_of_class(obj, a_class):`
that returns True if an object is an instance of, or if
the object is an instance of a class that inherited from,
the specified class, else False
"""


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of, or if
the object is an instance of a class that inherited from,
the specified class ; otherwise False."""
    return isinstance(obj, a_class)
