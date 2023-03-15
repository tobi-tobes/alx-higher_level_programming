#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deleted = []
    for k, v in a_dictionary.items():
        if v == value:
            deleted.append(k)
        else:
            continue
    if len(deleted) == 0:
        return (a_dictionary)
    for i in deleted:
        del a_dictionary[i]
    return (a_dictionary)
