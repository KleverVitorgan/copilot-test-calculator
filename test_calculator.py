"""
Unit tests for the calculator module.
"""
import unittest
from calculator import add, subtract, multiply, divide, calculate


class TestCalculator(unittest.TestCase):
    """Test cases for calculator operations."""
    
    def test_add(self):
        """Test addition."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0.1, 0.2), 0.30000000000000004)  # Float precision
    
    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)
    
    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(0, 5), 0)
    
    def test_divide(self):
        """Test division."""
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(-6, -3), 2)
        self.assertEqual(divide(5, 2), 2.5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_calculate_addition(self):
        """Test calculate function with addition."""
        self.assertEqual(calculate(5, '+', 3), 8)
        self.assertEqual(calculate(-1, '+', 1), 0)
    
    def test_calculate_subtraction(self):
        """Test calculate function with subtraction."""
        self.assertEqual(calculate(5, '-', 3), 2)
        self.assertEqual(calculate(0, '-', 5), -5)
    
    def test_calculate_multiplication(self):
        """Test calculate function with multiplication."""
        self.assertEqual(calculate(2, '*', 3), 6)
        self.assertEqual(calculate(-2, '*', 3), -6)
    
    def test_calculate_division(self):
        """Test calculate function with division."""
        self.assertEqual(calculate(6, '/', 3), 2)
        self.assertEqual(calculate(5, '/', 2), 2.5)
    
    def test_calculate_division_by_zero(self):
        """Test calculate function with division by zero."""
        with self.assertRaises(ValueError):
            calculate(5, '/', 0)
    
    def test_calculate_unknown_operator(self):
        """Test calculate function with unknown operator."""
        with self.assertRaises(ValueError):
            calculate(5, '^', 2)
        with self.assertRaises(ValueError):
            calculate(5, '%', 2)


if __name__ == '__main__':
    unittest.main()
