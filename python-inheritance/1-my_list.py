#!/usr/bin/python3
"""Defines a class MyList."""


class MyList(list):
    '''Custom MyList class.'''

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
