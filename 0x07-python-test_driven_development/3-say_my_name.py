#!/usr/bin/python3
"""
say_my_name module
This module contains the function say_my_name,
 which prints `My name is <first name> <last name>`
"""


def say_my_name(first_name, last_name=""):
    """prints `My name is <first name> <last name>`"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    elif len(first_name) == 0:
        raise TypeError("please put a first name")
    print('My name is {} {}'.format(first_name, last_name))
