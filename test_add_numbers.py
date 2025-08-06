import unittest
from add_numbers import add_two_numbers

class TestAddNumbers(unittest.TestCase):
    """Test cases for the add_two_numbers function."""
    
    def test_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add_two_numbers(5, 3), 8)
        self.assertEqual(add_two_numbers(10.5, 2.5), 13.0)
    
    def test_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add_two_numbers(-5, -3), -8)
        self.assertEqual(add_two_numbers(-10.5, -2.5), -13.0)
    
    def test_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        self.assertEqual(add_two_numbers(5, -3), 2)
        self.assertEqual(add_two_numbers(-5, 3), -2)
        self.assertEqual(add_two_numbers(10.5, -5.5), 5.0)
    
    def test_zero(self):
        """Test adding with zero."""
        self.assertEqual(add_two_numbers(0, 5), 5)
        self.assertEqual(add_two_numbers(5, 0), 5)
        self.assertEqual(add_two_numbers(0, 0), 0)
    
    def test_decimal_numbers(self):
        """Test adding decimal numbers."""
        self.assertAlmostEqual(add_two_numbers(0.1, 0.2), 0.3, places=1)
        self.assertAlmostEqual(add_two_numbers(1.5, 2.7), 4.2, places=1)

if __name__ == "__main__":
    unittest.main()
