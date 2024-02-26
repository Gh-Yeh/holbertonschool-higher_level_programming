#!/usr/bin/python3
"""Module for Base unit tests."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_intialization(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base()

    def tearDown(self):
        """Tear down the test case."""
        del self.b1
        del self.b2

    def test_constructor(self):
        '''Testing constructor.'''
        with self.assertRaises(TypeError):
            Base.__init__()
        with self.assertRaises(TypeError):
            Base.__init__(self, 1, 2)

    def test_nb_objects_initialized(self):
        '''Tests if nb_objects is starting from zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 2)

    def test_noarg_inst(self):
        '''Tests Base() instantiation.'''
        self.assertEqual(str(type(self.b1)), "<class 'models.base.Base'>")
        self.assertEqual(self.b1.__dict__, {"id": 1})
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b1.id, self.b2.id - 1)

    def test_None_id(self):
        '''Tests Base(None) instantiation.'''
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        '''Test a unique id.'''
        b1 = Base(12)
        self.assertEqual(12, b1.id)

    def test_inst_multi_instances(self):
        '''Test a unique id after creating different instances.'''
        b3 = Base(12)
        self.assertEqual([self.b1.id, self.b2.id, b3.id], [1, 2, 12])

    def test_inst_multi_sync(self):
        '''Test a unique id after creating different instances.'''
        b3 = Base("foo")
        b4 = Base()
        self.assertEqual(Base._Base__nb_objects, b4.id)

    def test_id_public(self):
        '''Test accessing a public id.'''
        self.b1.id = 15
        self.assertEqual(15, self.b1.id)

    def test_private_attribute(self):
        '''Tests if nb_objects is private class attribute.'''
        with self.assertRaises(AttributeError):
            print(Base.__nb_instances)

    def test_str_id(self):
        '''Tests custom arguments'''
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        '''Tests custom arguments'''
        self.assertEqual(5.5, Base(5.5).id)

    def test_int_id(self):
        '''Tests id passed as int arg.'''
        i = 491
        b = Base(id=i)
        self.assertEqual(b.id, i)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaisesRegex(TypeError, r"to_json_string\(\) missing 1 required positional argument: 'list_dictionaries'"):
            Base.to_json_string()

    def test_to_json_string_rectangle_type(self):
        '''Tests to_json_string() signature:'''
        r = Rectangle(10, 17, 12, 18, 16)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        '''Tests to_json_string() signature:'''
        r = Rectangle(10, 17, 12, 18, 16)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 57)
        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))

    def test_to_json_string_rectangle_two_dicts(self):
        '''Tests to_json_string() signature:'''
        r1 = Rectangle(12, 13, 5, 19, 2)
        r2 = Rectangle(4, 12, 14, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 110)

    def test_to_json_string_square_type(self):
        '''Tests to_json_string() signature:'''
        s = Square(10, 12, 3, 14)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        '''Tests to_json_string() signature:'''
        s = Square(101, 21, 13, 14)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 43)

    def test_to_json_string_square_two_dicts(self):
        '''Tests to_json_string() signature:'''
        s1 = Square(10, 12, 13, 14)
        s2 = Square(41, 15, 21, 12)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 84)

    def test_to_json_string_empty_list(self):
        '''Tests to_json_string() signature:'''
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        '''Tests to_json_string() signature:'''
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        '''Tests save_to_file() method.'''
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        '''Tests save_to_file() method.'''
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        '''Tests save_to_file() method.'''
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        '''Tests save_to_file() method.'''
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        '''Tests save_to_file() method.'''
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        '''Tests save_to_file() method.'''
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        '''Tests save_to_file() method.'''
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        '''Tests save_to_file() method.'''
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        '''Tests save_to_file() method.'''
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        '''Tests save_to_file() method.'''
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaisesRegex(TypeError, r"from_json_string\(\) missing 1 required positional argument: 'json_string'"):
            Base.from_json_string()

    def test_from_json_string_type(self):
        '''Tests to_json_string() signature:'''
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        '''Tests to_json_string() signature:'''
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        '''Tests to_json_string() signature:'''
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        '''Tests to_json_string() signature:'''
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        '''Tests to_json_string() signature:'''
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        '''Tests to_json_string() signature:'''
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        '''Tests to_json_string() signature:'''
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        '''Tests create() method.'''
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_new(self):
        '''Tests create() method.'''
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        '''Tests create() method.'''
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        '''Tests create() method.'''
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        '''Tests create() method.'''
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        '''Tests create() method.'''
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        '''Tests create() method.'''
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        '''Tests create() method.'''
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        '''Tests load_from_file method.'''
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        '''Tests load_from_file method.'''
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        '''Tests load_from_file method.'''
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        '''Tests load_from_file method.'''
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        '''Tests load_from_file method.'''
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        '''Tests load_from_file method.'''
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        '''Tests load_from_file method.'''
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        '''Tests load_from_file method.'''
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main()
