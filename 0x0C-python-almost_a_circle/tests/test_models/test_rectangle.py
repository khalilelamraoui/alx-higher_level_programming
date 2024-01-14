#!/usr/bin/python3
"""
test for rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Rectangle class tests
    """
    def test_1(self):
        """
        test 1
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        r4 = Rectangle(10, 2, 0, 0, -12)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)

    def test_2(self):
        """
        test 2
        """
        r1 = Rectangle(10, 2)
        r1.width = 5
        self.assertEqual(r1.width, 5)
        r1.height = 3
        self.assertEqual(r1.height, 3)
        r1.x = 1
        self.assertEqual(r1.x, 1)
        r1.y = 2
        self.assertEqual(r1.y, 2)

    def test_3(self):
        """
        test 3
        """
        r1 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r1.width = "hello"
        with self.assertRaises(TypeError):
            r1.width = True
        with self.assertRaises(TypeError):
            r1.width = 1.5
        with self.assertRaises(TypeError):
            r1.height = "hello"
        with self.assertRaises(TypeError):
            r1.height = True
        with self.assertRaises(TypeError):
            r1.height = 1.5
        with self.assertRaises(TypeError):
            r1.x = "hello"
        with self.assertRaises(TypeError):
            r1.x = True
        with self.assertRaises(TypeError):
            r1.x = 1.5
        with self.assertRaises(TypeError):
            r1.y = "hello"
        with self.assertRaises(TypeError):
            r1.y = True
        with self.assertRaises(TypeError):
            r1.y = 1.5
        
    def test_4(self):
        """
        test 4
        """
        r1 = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r1.width = -10
        with self.assertRaises(ValueError):
            r1.height = -2
        with self.assertRaises(ValueError):
            r1.x = -1
        with self.assertRaises(ValueError):
            r1.y = -2

    def test_5(self):
        """
        test 5
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(3, 2, 0, 0, 12)
        self.assertEqual(r3.area(), 6)
        r4 = Rectangle(2, 3, 0, 0, -12)
        self.assertEqual(r4.area(), 6)

    def test_6(self):
        """
        test 6
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.display(), None)
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.display(), None)
        r3 = Rectangle(3, 2, 0, 0, 12)
        self.assertEqual(r3.display(), None)
        r4 = Rectangle(2, 3, 0, 0, -12)
        self.assertEqual(r4.display(), None)

    def test_7(self):
        """
        test 7
        """
        r1 = Rectangle(2, 3, 2, 2)
        self.assertEqual(r1.display(), None)
        r2 = Rectangle(3, 2, 1, 0)
        self.assertEqual(r2.display(), None)
        r3 = Rectangle(3, 2, 0, 1, 12)
        self.assertEqual(r3.display(), None)
        r4 = Rectangle(2, 3, 0, 0, -12)
        self.assertEqual(r4.display(), None)


if __name__ == '__main__':
    unittest.main()