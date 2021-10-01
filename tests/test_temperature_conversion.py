from unittest import TestCase

from PythonPackage.chapter_four.temperature_conversion import convert_to_fahrenheit


class Test(TestCase):
    def test_convert_to_fahrenheit(self):
        celsius = 32
        fahrenheit = (9 / 5) * celsius + 32
        self.assertEqual(convert_to_fahrenheit(32), fahrenheit)
