#!/usr/bin/python3
"""
Module that contains a function that
returns True if the object is exactly an instance
"""


def is_same_class(obj, a_class):
    """
    if the object is exactly an instance
    then return True
    """
    return type(obj) == a_class
