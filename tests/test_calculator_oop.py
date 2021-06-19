import unittest
from calculator_oop import Calculator


class CalculatorOPPTest(unittest.TestCase):
     def test_something(self):
        self.assertEqual(Calculator.add(2, 3), 5)

     def test_add_result_type(self):
        self.assertIsInstance(Calculator.add(2, 3), int)

     def test_sub_result(self):
         self.assertEqual(Calculator.sub(2, 3), -1)

     def test_div_result(self):
         self.assertEqual(Calculator.div(4567, 3), 4567//3)

     def test_sub_result_type(self):
         self.assertEqual(Calculator.mul(2, 3), 6)


if __name__ == '__main__':
    unittest.main()
