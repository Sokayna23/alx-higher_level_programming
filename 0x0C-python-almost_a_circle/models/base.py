#!/usr/bin/python3
"""Module that defines Base class."""
import json
import csv


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
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
            elif cls.__name__ == "Square":
                instance = cls(1)
            instance.update(**dictionary)
        return instance

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): list of instances to serialize.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
                return
            else:
                fieldnames = list_objs[0].to_dictionary().keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
            Deserializes objects from a CSV file and

            Returns:
                a list of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                reader = csv.DictReader(f)
                objs = []
                for row in reader:
                    obj = {key: int(value) for key, value in row.items()}
                    objs.append(obj)
                return [cls.create(**item) for item in objs]
        except FileNotFoundError:
            return []
