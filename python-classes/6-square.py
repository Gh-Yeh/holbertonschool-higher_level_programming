#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square with # symbol."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the current square."""
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size, end="")
                print()
