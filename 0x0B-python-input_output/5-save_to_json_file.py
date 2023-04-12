#!/usr/bin/python3
"""
save_to_json_file module
This module contains the function save_to_json_file,
which writes an Object to a text file, using a JSON
representation
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
