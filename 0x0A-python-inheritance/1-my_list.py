#!/usr/bin/python3
"""
MyList Class
This module defines a class MyList that inherits from list
"""


class MyList(list):
    """a class that inherits from list"""
    def print_sorted(self):
        """prints the list in sorted order"""
        print(sorted(self))
