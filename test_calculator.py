"""
Unit tests for the calculator module.
"""
import unittest
from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    """Test cases for calculator operations."""
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(0.5, 0.3), 0.8)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(5, -3), 2)
    
    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 20), -10)
        self.assertEqual(subtract(0.8, 0.3), 0.5)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(5, -3), 8)
    
    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 0), 0)
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(10, 20), 200)
        self.assertEqual(multiply(0.5, 0.4), 0.2)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(multiply(-5, -3), 15)
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(5, -3), -15)
    
    def test_multiply_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 0), 0)
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 0.333333, places=5)
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(divide(-6, -3), 2)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(6, -3), -2)
    
    def test_divide_by_zero(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_divide_zero_by_number(self):
        """Test division of zero by a number."""
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(0, -5), 0)
    
    def test_float_precision(self):
        """Test operations with floating point numbers."""
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)
        self.assertAlmostEqual(multiply(0.1, 0.1), 0.01, places=10)


if __name__ == '__main__':
    unittest.main()
