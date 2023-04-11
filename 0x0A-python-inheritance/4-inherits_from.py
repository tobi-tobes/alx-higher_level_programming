#!/usr/bin/python3
"""
inherits_from Function
This module defines a function `def inherits_from(obj, a_class):`
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
that inherited (directly or indirectly)
from the specified class ; otherwise False."""
    return issubclass(type(obj), a_class)
