#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Class Student that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Create a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student."""
        if (not isinstance(attrs, list) or attrs is None):
            return self.__dict__
        return {item: self.__dict__[item] for item in attrs if item in self.__dict__}

    def reload_from_json(self, json):
        """Replace all attributes of the Student."""

        for name, value in json.items():
            setattr(self, name, value)
