#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of this Rectangle.
            height (int): The height of this Rectangle.
            x (int): The x coordinate of this Rectangle.
            y (int): The y coordinate of this Rectangle.
            id (int): The identity of this Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.__width = width
        self.__x = x
        self.__height = height
        self.__y = y

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @property
    def x(self):
        '''X of this rectangle.'''
        return self.__x

    @property
    def y(self):
        '''Y of this rectangle.'''
        return self.__y

    @width.setter
    def width(self, value):
        '''setter method for the attribute width'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''setter method for the attribute height'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        '''setter method for the attribute x'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        '''setter method for the attribute y'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        '''Prints the rectangle in #'''
        rect = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rect, end='')

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __func_update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method that set instance attributes.'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        if args:
            self.__func_update(*args)
        elif kwargs:
            self.__func_update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
