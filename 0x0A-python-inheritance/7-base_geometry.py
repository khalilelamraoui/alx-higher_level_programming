#!/usr/bin/python3
"""
Module 7-base_geometry contains class BaseGeometry
and methods area and integer_validator
"""


class BaseGeometry:
    """
    class BaseGeometry
    """

    def area(self):
        """
        raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
