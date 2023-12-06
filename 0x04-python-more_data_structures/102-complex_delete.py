#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        new_dict = {}
        for key, val in a_dictionary.items():
            if val != value:
                new_dict[key] = a_dictionary[key]
    return new_dict
