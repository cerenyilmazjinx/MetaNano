# test_metanano.py
"""
Tests for MetaNano module.
"""

import unittest
from metanano import MetaNano

class TestMetaNano(unittest.TestCase):
    """Test cases for MetaNano class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaNano()
        self.assertIsInstance(instance, MetaNano)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaNano()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
