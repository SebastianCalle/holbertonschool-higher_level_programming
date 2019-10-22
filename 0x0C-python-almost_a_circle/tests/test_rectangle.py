#!/usr/bin/python3

from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """Test class rectangle"""

    def test_instance_base(self):
        """Test if is isntances of base"""
        b1 = Rectangle(1, 2)
        self.assertEqual(True, isinstance(b1, Base))

    def test_attribute_Width(self):
        """Test if attributes are setter"""
        b1 = Rectangle(10, 2, 4, 5, 12)
        self.assertEqual(10, b1.width)

    def test_attribute_heigth(self):
        """Test if attributes are setter"""
        b1 = Rectangle(10, 2, 4, 5, 12)
        self.assertEqual(2, b1.height)

    def test_attribute_id(self):
        """Test if attributes are setter"""
        b1 = Rectangle(10, 2, 4, 5, 12)
        self.assertEqual(12, b1.id)

    def test_attribute_x(self):
        """Test if attributes are setter"""
        b1 = Rectangle(10, 2, 4, 5, 12)
        self.assertEqual(4, b1.x)

    def test_attribute_y(self):
        """Test if attributes are setter"""
        b1 = Rectangle(10, 2, 4, 5, 12)
        self.assertEqual(5, b1.y)

    def test_width_val_neg(self):
        """Test for negative value the width"""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 1)

    def test_height_val_neg(self):
        """Test for negative value the height"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, -1)

    def test_width_if_is_str(self):
        """Test for width is string"""
        with self.assertRaises(TypeError):
            r = Rectangle("1", 5)

    def test_heigth_if_is_str(self):
        """Test for height is string"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, "5")

    def test_x_if_is_str(self):
        """Test for x is string"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "1")

    def test_y_if_is_str(self):
        """Test for y is string"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 1, "4")

    def test_x_val_neg(self):
        """Test for negative value the x"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -1)

    def test_y_val_neg(self):
        """Test for negative value the y"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 1, -4)

    def test_area(self):
        """Test area of Rectangle"""
        b1 = Rectangle(2, 2, 4, 5, 12)
        self.assertEqual(4, b1.area())

    def test_update_args(self):
        """Test update of Rectangle"""
        b1 = Rectangle(2, 2, 4, 5, 12)
        b1.update(10, 5, 5)
        self.assertEqual(10, b1.id)
        self.assertEqual(5, b1.width)
        self.assertEqual(5, b1.height)

    def test_update_kwargs(self):
        """Test update of Rectangle"""
        b1 = Rectangle(2, 2, 4, 5, 12)
        b1.update(width=5, id=10, height=5)
        self.assertEqual(10, b1.id)
        self.assertEqual(5, b1.width)
        self.assertEqual(5, b1.height)

    def test_to_dictionary(self):
        """Test to dictionary of Rectangle"""
        b1 = Rectangle(2, 2, 4, 5, 12)
        dict1 = {
            'y': 5,
            'x': 4,
            'width': 2,
            'height': 2,
            'id': 12,
        }
        self.assertEqual(dict1, b1.to_dictionary())
