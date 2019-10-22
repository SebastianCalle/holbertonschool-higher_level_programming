#!/usr/bin/python3

from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import unittest


class TestSquare(unittest.TestCase):
    """Test class rectangle"""

    def test_instance_Rectangle(self):
        """Test if is isntances of Rectangle"""
        b1 = Square(1)
        self.assertEqual(True, isinstance(b1, Rectangle))

    def test_attribute_size(self):
        """Test if attributes are setter"""
        b1 = Square(10, 4, 5, 12)
        self.assertEqual(10, b1.size)

    def test_attribute_id(self):
        """Test if attributes are setter"""
        b1 = Square(10, 4, 5, 12)
        self.assertEqual(12, b1.id)

    def test_attribute_x(self):
        """Test if attributes are setter"""
        b1 = Square(10, 4, 5, 12)
        self.assertEqual(4, b1.x)

    def test_attribute_y(self):
        """Test if attributes are setter"""
        b1 = Square(10, 4, 5, 12)
        self.assertEqual(5, b1.y)

    def test_size_val_neg(self):
        """Test for negative value the size"""
        with self.assertRaises(ValueError):
            r = Square(-5)

    def test_size_if_is_str(self):
        """Test for size is string"""
        with self.assertRaises(TypeError):
            r = Square("1")

    def test_x_if_is_str(self):
        """Test for x is string"""
        with self.assertRaises(TypeError):
            r = Square(1, "1")

    def test_y_if_is_str(self):
        """Test for y is string"""
        with self.assertRaises(TypeError):
            r = Square(1, 1, "4")

    def test_x_val_neg(self):
        """Test for negative value the x"""
        with self.assertRaises(ValueError):
            r = Square(1, -1)

    def test_y_val_neg(self):
        """Test for negative value the y"""
        with self.assertRaises(ValueError):
            r = Square(1, 1, -4)

    def test_area(self):
        """Test area of Square"""
        b1 = Square(2, 4, 5, 12)
        self.assertEqual(4, b1.area())

    def test_update_args(self):
        """Test update of Square"""
        b1 = Square(2, 4, 5, 12)
        b1.update(10, 5, 5)
        self.assertEqual(10, b1.id)
        self.assertEqual(5, b1.size)

    def test_update_kwargs(self):
        """Test update of Square"""
        b1 = Square(1, 1, 1, 1)
        b1.update(id=10, x=5, size=20)
        self.assertEqual(10, b1.id)
        self.assertEqual(5, b1.x)
        self.assertEqual(20, b1.size)

    def test_to_dictionary(self):
        """Test to dictionary of Square"""
        b1 = Square(2, 4, 5, 12)
        dict1 = {
            'y': 5,
            'x': 4,
            'size': 2,
            'id': 12,
        }
        self.assertEqual(dict1, b1.to_dictionary())
