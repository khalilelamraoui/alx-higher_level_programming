#!/usr/bin/python3
"""
Module that contains base class
"""


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init method
        Args:
            id (int): id of object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string method
        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            json string representation of list_dictionaries
        """
        import json

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file method
        Args:
            list_objs (list): list of objects
        """
        filename = cls.__name__ + ".json"
        list_dicts = []

        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))