#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Class Student that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Create a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (not isinstance(attrs, list)):
            return self.__dict__
        return {item: self.__dict__[item] for item in attrs if item in self.__dict__}
