#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers or floats values.
    Args:
        a: the first integer.
        b: the second integer.Defaults to 98
    Raises:
        TypeError: If a and b are not integers or floats.
    Returns:
        An integer of the sum between a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
