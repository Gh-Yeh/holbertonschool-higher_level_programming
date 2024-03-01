#!/usr/bin/python3
"""
...
"""

from models.base import Base


class Rectangle(Base):
    """
    ...
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        ...
        """
        super().__init__(id)

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        ...
        """
        return self.__width

    @width.setter
    def width(self, param):
        """
        ...
        """
        self.check_integer_parameter(param, 'width')

        self.__width = param

    @property
    def height(self):
        """
        ...
        """
        return self.__height

    @height.setter
    def height(self, param):
        """
        ...
        """
        self.check_integer_parameter(param, 'height')

        self.__height = param

    @property
    def x(self):
        """
        ...
        """
        return self.__x

    @x.setter
    def x(self, param):
        """
        ...
        """
        self.check_integer_parameter(param, 'x')

        self.__x = param

    @property
    def y(self):
        """
        ...
        """
        return self.__y

    @y.setter
    def y(self, param):
        """
        ...
        """
        self.check_integer_parameter(param, 'y')

        self.__y = param

    def check_integer_parameter(self, value, param):
        """
        ...
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

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


if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
