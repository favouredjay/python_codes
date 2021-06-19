import unittest

from calculator_functions import add
from calculator_functions import sub
from calculator_functions import div
from calculator_functions import mul

class CalculatorFunctionTest(unittest.TestCase):
    def test_add_result(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(277777, 50000), 277777 + 50000)

    def test_add_result_type(self):
        self.assertIsInstance(add(2, 3), int)
        self.assertIsInstance(add(-2, -3), int)
        self.assertIsInstance(add(-2, 3), int)
        self.assertIsInstance(add(277777, 50000), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            add(3.2, "d")

    def test_sub_result(self):
        self.assertEqual(sub(3, 2), 1)
        self.assertEqual(sub(-2, -3), 1)
        self.assertEqual(sub(-2, 3), -5)
        self.assertEqual(sub(277777, 50000), 277777 - 50000)

    def test_sub_result_type(self):
        self.assertIsInstance(sub(2, 3), int)
        self.assertIsInstance(sub(-2, -3), int)
        self.assertIsInstance(sub(-2, 3), int)
        self.assertIsInstance(sub(277777, 50000), int)

    def test_div_result(self):
        self.assertEqual(div(18, 3), 6)
        self.assertEqual(div(20, 4), 5)
        self.assertEqual(div(10000, 898), 10000//898)
        self.assertEqual(div(-15, -5), 3)

    def test_div_result_type(self):
        self.assertIsInstance(div(18, 3), int)
        self.assertIsInstance(div(20, 4), int)
        self.assertIsInstance(div(10000, 898), int)
        self.assertIsInstance(div(-15, -5), int)

    def test_mul_result(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(20, 4), 80)
        self.assertEqual(mul(10000, 898), 10000*898)
        self.assertEqual(mul(-15, 5), -75)

    def test_mul_result_type(self):
        self.assertIsInstance(mul(18, 3), int)
        self.assertIsInstance(mul(20, 4), int)
        self.assertIsInstance(mul(10000, 898), int)
        self.assertIsInstance(mul(-15, 5), int)











if __name__ == '__main__':
    unittest.main()
