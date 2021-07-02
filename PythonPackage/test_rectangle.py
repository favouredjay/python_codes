import unittest
from rectangle import Rectangle


class rectangleTest(unittest.TestCase):
    def test_that_length_is_valid(self):
        rectangle = Rectangle()
        rectangle.set_length(20.00)
        self.assertEqual(20.00, rectangle.get_length())

    def test_that_width_is_invalid(self):
        rectangle = Rectangle()
        rectangle.set_width(5.00)
        self.assertEqual(5.00, rectangle.get_width())

    def test_that_area_can_be_calculated(self):
        rectangle = Rectangle()
        rectangle.set_width(6.00)
        rectangle.set_length(4.00)
        self.assertEqual(24.00, rectangle.calculate_area())

    def test_that_perimeter_can_be_calculated(self):
        rectangle = Rectangle()
        rectangle.set_width(4.00)
        rectangle.set_length(2.00)
        self.assertEqual(12.00, rectangle.calculate_perimeter())


if __name__ == '__main__':
    unittest.main()
