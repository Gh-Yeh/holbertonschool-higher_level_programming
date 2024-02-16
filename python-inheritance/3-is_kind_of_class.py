#!/usr/bin/python3
'''Module for is_kind_of_class method.'''


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or subclass of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The matching class
    Returns:
        If obj is an instance or child of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
