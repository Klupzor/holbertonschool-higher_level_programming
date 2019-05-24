#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 7, 3, 4]), 7)
        self.assertEqual(max_integer([-1, -7, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -7, 9.3, -4]), 9.3)
        self.assertEqual(max_integer((1, 1, 1, 1)), 1)
        self.assertEqual(max_integer("str"), "t")
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, [1, 2, "er", 8])
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, [1, 2, 8], [1, 2])

if __name__ == '__main__':
    unittest.main()
