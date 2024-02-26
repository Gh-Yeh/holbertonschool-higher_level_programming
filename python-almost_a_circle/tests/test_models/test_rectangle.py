#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""
import unittest
import io
import sys

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_inheritance(self):
        '''Tests if Rectangle inherits Base.'''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rect_instantiation(self):
        '''Tests rectangle instantiation.'''
        r = Rectangle(10, 20)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")

    def test_rectangle_is_base(self):
        '''Tests if Rectangle inherits Base.'''
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_class(self):
        '''Tests Rectangle class type.'''
        self.assertEqual(
            str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_with_no_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_with_one_arg(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_with_two_args(self):
        '''Tests constructor signature.'''
        r1 = Rectangle(20, 2)
        r2 = Rectangle(10, 20)
        self.assertEqual(r1.id, r2.id - 1)

    def test_with_three_args(self):
        '''Tests constructor signature.'''
        r1 = Rectangle(12, 32, 4)
        r2 = Rectangle(24, 14, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_with_four_args(self):
        '''Tests constructor signature.'''
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_with_five_args(self):
        '''Tests constructor signature.'''
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_with_more_than_five_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        '''Tests if width is private class attribute.'''
        with self.assertRaises(AttributeError):
            print(Rectangle(25, 5, 10, 0, 11).__width)

    def test_height_private(self):
        '''Tests if height is private class attribute.'''
        with self.assertRaises(AttributeError):
            print(Rectangle(25, 5, 10, 0, 11).__height)

    def test_x_private(self):
        '''Tests if x is private class attribute.'''
        with self.assertRaises(AttributeError):
            print(Rectangle(25, 5, 10, 0, 11).__x)

    def test_y_private(self):
        '''Tests if y is private class attribute.'''
        with self.assertRaises(AttributeError):
            print(Rectangle(25, 5, 10, 0, 11).__y)

    def test_width_getter(self):
        '''Tests if the width getter method.'''
        r = Rectangle(25, 5, 10, 0, 11)
        self.assertEqual(25, r.width)

    def test_width_setter(self):
        '''Tests if the width setter method.'''
        r = Rectangle(25, 5, 10, 0, 11)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        '''Tests if the height getter method.'''
        r = Rectangle(25, 5, 10, 0, 11)
        self.assertEqual(5, r.height)

    def test_height_setter(self):
        '''Tests if the height setter method.'''
        r = Rectangle(25, 5, 10, 0, 11)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        '''Tests if the x getter method.'''
        r = Rectangle(25, 5, 10, 0, 11)
        self.assertEqual(10, r.x)

    def test_x_setter(self):
        '''Tests if the x setter method.'''
        r = Rectangle(25, 5, 10, 0, 11)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        '''Tests if the y getter method.'''
        r = Rectangle(25, 5, 10, 0, 11)
        self.assertEqual(0, r.y)

    def test_y_setter(self):
        '''Tests if the y setter method.'''
        r = Rectangle(25, 5, 10, 0, 11)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_id_inherited(self):
        '''Tests if id is inherited from Base.'''
        Base._Base__nb_objects = 98
        r = Rectangle(2, 4)
        self.assertEqual(r.id, 99)


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing the Rectangle width attribute."""

    def test_None_width(self):
        '''Tests if width is an integer.'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        '''Tests if width is an integer.'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        '''Tests if width is an integer.'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        '''Tests if width is an integer.'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        '''Tests if width is an integer.'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        '''Tests if width is an integer.'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        '''Tests if width is an integer.'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        '''Tests if width is an integer.'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        '''Tests if width is an integer.'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_negative_width(self):
        '''Tests if width is positive number.'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        '''Tests if width is not number.'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing the Rectangle height attribute."""

    def test_None_height(self):
        '''Tests if height is an integer.'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        '''Tests if height is an integer.'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        '''Tests if height is an integer.'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        '''Tests if height is an integer.'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_height(self):
        '''Tests if height is an integer.'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        '''Tests if height is an integer.'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        '''Tests if height is an integer.'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        '''Tests if height is an integer.'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset_height(self):
        '''Tests if height is an integer.'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range_height(self):
        '''Tests if height is an integer.'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_negative_height(self):
        '''Tests if height is positive.'''
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        '''Tests if height is greater than zero.'''
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def test_None_x(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_negative_x(self):
        '''Tests if x is greater than zero.'''
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_None_y(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        '''Tests if x is an integer.'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_negative_y(self):
        '''Tests if x is greater than zero.'''
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of Rectangle class."""

    def test_area(self):
        '''Tests the area method return.'''
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_bignum(self):
        '''Tests the area method return.'''
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_with_different_attributes(self):
        '''Tests the area method return.'''
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_area_arg(self):
        '''Tests the area arg.'''
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for the output if rectangle."""

    @staticmethod
    def cap_out(rect, method):
        """Store output in a file and return it.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout.
        """
        capt = io.StringIO()
        sys.stdout = capt
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capt

    def test_print_width_height(self):
        '''Tests the print.'''
        r = Rectangle(5, 6)
        capture = TestRectangle_stdout.cap_out(r, "print")
        trystr = "[Rectangle] ({}) 0/0 - 5/6\n".format(r.id)
        self.assertEqual(trystr, capture.getvalue())

    def test_str_width_height_x(self):
        '''Tests the str function.'''
        r = Rectangle(15, 15, 1)
        trystr = "[Rectangle] ({}) 1/0 - 15/15".format(r.id)
        self.assertEqual(trystr, str(r))

    def test_str_width_height_x_y(self):
        '''Tests the str function.'''
        r = Rectangle(11, 28, 12, 44)
        trystr = "[Rectangle] ({}) 12/44 - 11/28".format(r.id)
        self.assertEqual(trystr, str(r))

    def test_str_width_height_x_y_id(self):
        '''Tests the str function.'''
        r = Rectangle(13, 1, 12, 4, 7)
        self.assertEqual("[Rectangle] (7) 12/4 - 13/1", str(r))

    def test_str_modified_attributes(self):
        '''Tests the str function.'''
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_one_arg(self):
        '''Tests the str function.'''
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_display_width_height(self):
        '''Tests the display function.'''
        r = Rectangle(2, 3, 0, 0, 0)
        capt = TestRectangle_stdout.cap_out(r, "display")
        self.assertEqual("##\n##\n##\n", capt.getvalue())

    def test_display_width_height_x(self):
        '''Tests the display function.'''
        r = Rectangle(3, 2, 1, 0, 1)
        capt = TestRectangle_stdout.cap_out(r, "display")
        self.assertEqual(" ###\n ###\n", capt.getvalue())

    def test_display_width_height_y(self):
        '''Tests the display function.'''
        r = Rectangle(4, 5, 0, 1, 0)
        capt = TestRectangle_stdout.cap_out(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capt.getvalue())

    def test_display_width_height_x_y(self):
        '''Tests the display function.'''
        r = Rectangle(2, 4, 3, 2, 0)
        capt = TestRectangle_stdout.cap_out(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capt.getvalue())

    def test_display_one_arg(self):
        '''Tests the display function.'''
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    def test_update_args_zero(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(89, 2, 3, 4, 5, 6)

    def test_update_args_None_id_and_more(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_invalid_width_type(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height_x_y(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_height_before_x_y(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_x_before_y(self):
        """testing args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_one(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_two(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        """testing kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        """testing args kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        """testing args and kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(height=5, id=89, a=1, b=54, x=19, y=7)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_dictionary(self):
        '''Tests to_dictionary() signature:'''
        with self.assertRaisesRegex(TypeError, r"to_dictionary\(\) missing 1 required positional argument: 'self'"):
            Rectangle.to_dictionary()

    def test_dictionary_output(self):
        '''Tests to_dictionary() signature:'''
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_object_changes(self):
        '''Tests to_dictionary() signature:'''
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        '''Tests to_dictionary() signature:'''
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
