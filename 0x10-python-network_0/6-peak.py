#!/usr/bin/python3
"""
6-peak.py
This module contains a function that finds
a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return
    if type(list_of_integers) != list:
        return
    high = len(list_of_integers) - 1
    low = 0

    while low < high:
        mid = (high + low) // 2
        if list_of_integers[mid] >= list_of_integers[mid - 1] and\
           list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[low]
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            high = mid
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
