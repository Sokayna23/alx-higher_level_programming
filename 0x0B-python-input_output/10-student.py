#!/usr/bin/python3
"""Module that defines Student class."""


class Student:
    """Defines a class Student."""

    def __init__(self, first_name, last_name, age):
        """Istantiation of Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the class Student."""
        if (type(attrs) == list and
                all(type(elmt) == str for elmt in attrs)):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
