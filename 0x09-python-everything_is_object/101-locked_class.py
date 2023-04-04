#!/usr/bin/python3
"""
LockedClass
This module defines a class LockedClass
"""


class LockedClass:
    """A class with no instance or class attributes that prevents
the user from dynamically creating new instance attributes unless
the new instance attribute is called `first_name`"""
    __slots__ = ['first_name']
