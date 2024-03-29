#!/usr/bin/python3
"""
Student Class module
This module contains the class Student
"""


class Student:
    """defines an instance of Student"""
    def __init__(self, first_name, last_name, age):
        """Initiates an instance of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
