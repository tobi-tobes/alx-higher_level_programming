#!/usr/bin/python3
"""
load_from_json_file module
This module contains the function load_from_json_file,
which creates an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        my_obj = json.load(f)
    return my_obj
