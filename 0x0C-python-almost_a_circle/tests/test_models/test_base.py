from models.base import Base
import unittest

class Test_base(unittest.TestCase):
    """Unittest Base class"""
    b1 = Base()
    self.assertequal()
    b2 = Base()
    print(b2.id)
    b3 = Base()
    print(b3.id)
    b4 = Base(12)
    print(b4.id)
    b5 = Base()
    print(b5.id)
