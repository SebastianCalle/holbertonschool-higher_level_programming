#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test module max_integer"""

    def test_max_integer(self):
        """test max integer positiv"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_negative(self):
        """test max integer negative"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_same_elements(self):
        """test max integer whit all elements equals"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_float_numbers(self):
        """test max floats"""
        self.assertEqual(max_integer([1.1, 1.2, 1.4, 1.9]), 1.9)

    def test_characters(self):
        """test max characters"""
        self.assertEqual(max_integer(['s', 'a', 'a']), 's')

    def test_if_list_is_none(self):
        """test max characters"""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
