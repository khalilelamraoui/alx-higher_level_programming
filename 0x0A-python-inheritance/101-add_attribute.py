#!/usr/bin/python3
"""
Module for add_attribute method.
"""


def add_attribute(obj, name, value):
    """
    add_attribute method to add attributes to objects
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
