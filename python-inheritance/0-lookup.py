#!/usr/bin/python3
'''Defines a module for lookup function'''


def lookup(obj):
    '''Looks up object attributes and methods.
    Args:
        obj (object): the passed object.

    Returns:
        list: the list of attributes.
    '''
    return dir(obj)
