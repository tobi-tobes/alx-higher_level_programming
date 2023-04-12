#!/usr/bin/python3
"""
to_json_string module
This module contains the function to_json_string,
which returns the JSON representation of an object
(string)
"""


import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    string_ver = json.dumps(my_obj)
    return string_ver
