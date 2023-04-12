#!/usr/bin/python3
"""
7-add_item.py module
This module contains the script 7-add_item.py,
which adds all arguments to a Python list, and
then saves them to a file
"""


if __name__ == "__main__":
    import sys
    import os
    load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    if len(sys.argv) == 1:
        sys.exit(1)
    filename = "./add_item.json"
    if os.path.isfile(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, filename)
