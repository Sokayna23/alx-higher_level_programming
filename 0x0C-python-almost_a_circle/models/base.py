#!/usr/bin/python3
"""Module that defines Base class."""
import json


class Base:
    """
        Base class definition.

        Attributes:
            nb_objects (int): number of objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation
            Args:
                id (int): id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns the JSON string representation of a list of dictionaries.

            Args:
                list_dictionaries (list): a list of dictionaries.

            Returns:
                the JSON string representation of the list(success),
                an empty list [] (if it is None) otherwise.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list to a file.
            Args:
                list_objs (list): list of instances who inherits of Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicts_list = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(dicts_list))

    @staticmethod
    def from_json_string(json_string):
        """
            Returns the list of the JSON string representation a JSON string.

            Args:
                json_string (str): a string that represents a list of dicts.

            Returns:
                an empty list [] if the JSON string is None or empty,
                otherwise the list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns an instance with all attributes already set.

            Args:
                **dictionary: dictionary.
        """
        dummy_instance = cls.__new__(cls)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
            Returns a list of instances created from a JSON file.
        """
        filename = cls.__name__ + ".json"
        instances = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                dicts_list = Base.from_json_string(f.read())
                instances = [cls.create(**dic) for dic in dicts_list]
        except FileNotFoundError:
            pass
        return instances
