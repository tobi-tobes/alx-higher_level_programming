#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return (None)
    elif len(my_list) == 0:
        return (my_list)
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.apoend(i)
    return (new_list)
