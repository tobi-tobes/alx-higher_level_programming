#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        new_copy = my_list
        return (new_copy)
    elif idx > len(my_list) - 1:
        new_copy = my_list
        return (new_copy)
    else:
        new_copy = my_list
        new_copy[idx] = element
        return (new_copy)
