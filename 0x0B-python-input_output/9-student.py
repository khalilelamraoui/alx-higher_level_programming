#!/usr/bin/python3
"""
Module that defines a class Student
"""


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ Instantiation function
        Arguments:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Function that returns the dictionary description
        with simple data structure
        """
        return self.__dict__
