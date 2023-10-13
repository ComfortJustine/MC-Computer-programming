import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 4), 8)

    def test_subract(self):
        self.assertEqual(self.calculator.subtract(10, 6), 4)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(10, 8), 80)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(9, 3), 3) 
        self.assertRaises(ValueErroe, self.calculator.divide, 4, 0)

if __name__ == '__main__':
    unittest.main()       
