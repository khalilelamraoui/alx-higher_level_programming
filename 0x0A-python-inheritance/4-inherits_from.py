#!/usr/bin/python3
"""
function that returns True
if the object is an instance of a class
that inherited from the specified class
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    if the object is an instance of a class
    that inherited from the specified class
    then return True
    """
    isSub = issubclass(type(obj), a_class)

    return isSub and type(obj) != a_class
