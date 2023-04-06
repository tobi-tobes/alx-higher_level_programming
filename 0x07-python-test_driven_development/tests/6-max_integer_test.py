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

    def test_max_in_the_middle(self):
        """Tests whether the function handles max in the middle"""
        test_list = [2, 4, 6, 18, 6, 9, 11]
        self.assertEqual(max_integer(test_list), 18)

    def test_max_at_end(self):
        """Tests whether the function handles max at end"""
        test_list = [2, 9, 11, 5, 4, 3, 12]
        self.assertEqual(max_integer(test_list), 12)

    def test_max_at_beginning(self):
        """Tests whether the function handles max at beginning"""
        test_list = [13, 9, 11, 5, 4, 3, 12]
        self.assertEqual(max_integer(test_list), 13)

    def test_list_with_negs(self):
        """Tests whether the function returns the largest
 number in a list of positive and negative integers"""
        test_list = [2, 4, 6, -8, 7, 9, 1]
        self.assertEqual(max_integer(test_list), 9)

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
