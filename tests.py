import unittest
import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        radius = 4
        expected = math.pi * 16

        self.assertEqual(expected, task.circle_area(radius))

    def test4(self):
        radius = 0
        expected = 0

        self.assertEqual(expected, task.circle_area(radius))

    def test5(self):
        contents = [0, 1, 2, 3, 4, 5]

        expected = (0, 5)
        self.assertEqual(expected, task.first_and_last(contents))

    def test6(self):
        contents = []

        expected = None
        self.assertEqual(expected, task.first_and_last(contents))


if __name__ == '__main__':
    unittest.main()
