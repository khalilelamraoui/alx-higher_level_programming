#!/usr/bin/python3
"""
Module that contains a function that
returns True if the object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    if the object is an instance of a class
    then return True
    """
    return isinstance(obj, a_class)
