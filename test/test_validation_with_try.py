import unittest
from input_validation.validation_with_try import average


class TestExceptions(unittest.TestCase):

    def test_average_negative_first(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)

    def test_average_negative_second(self):
        with self.assertRaises(ValueError):
            average(90, -89, 78)

    def test_average_negative_third(self):
        with self.assertRaises(ValueError):
            average(90, -89, -78)
