#!/usr/bin/python3
"""
Unittest for max_integer
This module contains unittests for the function `def max_integer(list=[]):`
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """subclass of TestCase class in unittest module
 used to test max_integer function"""
    def test_empty_list(self):
        """Tests whether the function returns None if list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_normal_input(self):
        """Tests whether the function returns the largest
 number in a list of integers"""
        test_list = [2, 4, 6, 8, 6, 9, 11]
        self.assertEqual(max_integer(test_list), 11)

    def test_raise_list_with_nonint(self):
        """Tests whether the function raises a TypeError when
 encountering a non-integer in a list"""
        test_list = [2, "4", 6, None, 6, 9, 11]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_raise_not_a_list(self):
        """Tests whether the function raises an error if input is not a list"""
        test_list = (4, 6, 9, 8, 7)
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_raise_a_string(self):
        """Tests whether the function raises an error if input is a string"""
        test_list = "(4, 6, 9, 8, 7)"
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_list_with_negs(self):
        """Tests whether the function returns the largest
 number in a list of positive and negative integers"""
        test_list = [2, 4, 6, -8, 7, 9, -11]
        self.assertEqual(max_integer(test_list), 9)

    def test_raise_list_with_float(self):
        """Tests whether the function raises a TypeError
 when encountering a float"""
        test_list = [2, 5.5, 6, 9, 11]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_list_with_one(self):
        """Tests whether the function returns the only integer in a list"""
        test_list = [2]
        self.assertEqual(max_integer(test_list), 2)

    def test_list_with_all_negs(self):
        """Tests whether the function returns the largest
 number in a list of negative integers"""
        test_list = [-2, -4, -6, -8, -7, -9, -11]
        self.assertEqual(max_integer(test_list), -2)

    def test_list_with_two(self):
        """Tests whether the function works with a list with two integers"""
        test_list = [2, 2]
        self.assertEqual(max_integer(test_list), 2)
