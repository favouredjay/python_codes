from unittest import TestCase

from PythonPackage.chapter_four.rounding_numbers import rounding_integer


class Test(TestCase):

    def rounding_to_an_integer(self):
        number = 13.56449
        round_integer =  round(number)
        self.assertEqual(rounding_integer(),number, round_integer)
