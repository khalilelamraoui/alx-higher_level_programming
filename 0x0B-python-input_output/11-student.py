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

    def to_json(self, attrs=None):
        """
        Function that returns the dictionary description
        with simple data structure
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict

    def reload_from_json(self, json):
        """
        Function that replaces all attributes of the Student instance
        """
        for i in json:
            self.__dict__[i] = json[i]