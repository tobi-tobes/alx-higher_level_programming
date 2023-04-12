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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list:
            my_dict = {i: self.__dict__[i]
                       for i in attrs if i in self.__dict__}
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for k, v in json.items():
            self.__dict__[k] = v
