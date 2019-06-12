#!/usr/bin/python3
'''unittest for Base'''
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    '''Test Base'''
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(15)
        self.b4 = Base()

        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)

    def test1(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 15)
        self.assertEqual(self.b4.id, 3)

    def tets15(self):
        self.assertEqual(self.b4.id, 3)
        


if __name__ == '__main__':
    unittest.main()
