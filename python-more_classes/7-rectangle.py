#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        strshp = ""
        if self.__height == 0 or self.__width == 0:
            return strshp
        for i in range(self.__height):
            strshp += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                strshp += '\n'
        return strshp

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
