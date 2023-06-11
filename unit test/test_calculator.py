import unittest
import basic_calculator

class TestCalculator(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(basic_calculator.addiction(2, 2), 4)
        self.assertEqual(basic_calculator.addiction(2, 3), 5)
        self.assertEqual(basic_calculator.addiction(0, 2), 2)
        self.assertEqual(basic_calculator.addiction(-2, 2), 0)

    def test_subtraction(self):
        self.assertEqual(basic_calculator.subtraction(2, 2), 0)
        self.assertEqual(basic_calculator.subtraction(10, -12), 22)
        self.assertEqual(basic_calculator.subtraction(2.5, 2), 0.5)
        self.assertEqual(basic_calculator.subtraction(-2, -2), 0)

    def test_multuiplication(self):
        self.assertEqual(basic_calculator.multiplication(2, 2), 4)
        self.assertEqual(basic_calculator.multiplication(2, -2), -4)
        self.assertEqual(basic_calculator.multiplication(-2, -2), 4)
        self.assertEqual(basic_calculator.multiplication(0, 2), 0)

    def test_division(self):
        self.assertEqual(basic_calculator.division(2, 2), 1)
        self.assertEqual(basic_calculator.division(2, -2), -1)
        self.assertEqual(basic_calculator.division(1, 2), 0.5)

        with self.assertRaises(ValueError):
            basic_calculator.division(2, 0)

    def test_power(self):
        self.assertEqual(basic_calculator.power(2, 2), 4)
        self.assertEqual(basic_calculator.power(2, 0), 1)
        self.assertEqual(basic_calculator.power(0, 2), 0)
        
        with self.assertRaises(ValueError):
            basic_calculator.power(2, -2)

    def test_sqroot(self):
        self.assertEqual(basic_calculator.sqroot(4), 2)
        self.assertEqual(basic_calculator.sqroot(0), 0)

        with self.assertRaises(ValueError):
            basic_calculator.sqroot(-4)


if __name__ == '__main__':
    unittest.main()