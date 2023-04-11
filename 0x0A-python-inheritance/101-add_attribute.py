#!/usr/bin/python3
"""
add_attribute Function
This module defines a function add_attribute that adds
a new attribute to an object if it's possible
"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object if itâ€™s possible"""
    if hasattr(obj, '__dict__'):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
