from models.base import Base
import unittest


class Test_base(unittest.TestCase):
    """Test for base model"""

    def test_instance(self):
        b1 = Base()
        self.assertEqual(1, b1.id)
        b2 = Base()
        self.assertEqual(2, b2.id)
        b3 = Base(7)
        self.assertEqual(7, b3.id)
