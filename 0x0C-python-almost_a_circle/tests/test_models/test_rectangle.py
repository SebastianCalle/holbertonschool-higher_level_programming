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

    def test_attributes(self):
        """Test if attributes are setter"""
        b1 = Rectangle(10, 2, 4, 5, 12)
        self.assertEqual(12, b1.id)
        self.assertEqual(10, b1.width)
        self.assertEqual(2, b1.height)
        self.assertEqual(4, b1.x)
        self.assertEqual(5, b1.y)

    def test_setter_and_getter(self):
        """Test setter and getter"""
        b1 = Rectangle(10, 2, 4, 5, 12)

