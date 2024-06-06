import unittest
from main import sort


class TestSort(unittest.TestCase):

    def test_standard_package(self):
        """Tests sorting a standard package."""
        stack = sort(100, 50, 30, 15)
        self.assertEqual(stack, "STANDARD")

    def test_heavy_package(self):
        """Tests sorting a heavy package."""
        stack = sort(100, 50, 30, 25)
        self.assertEqual(stack, "SPECIAL")

    def test_bulky_package(self):
        """Tests sorting a bulky package."""
        stack = sort(200, 50, 30, 15)
        self.assertEqual(stack, "SPECIAL")

    def test_bulky_by_dimension(self):
        """Tests sorting a bulky package by dimension."""
        stack = sort(100, 155, 30, 15)
        self.assertEqual(stack, "SPECIAL")

    def test_rejected_package(self):
        """Tests sorting a package that is both heavy and bulky."""
        stack = sort(200, 155, 30, 25)
        self.assertEqual(stack, "REJECTED")

    def test_invalid_dimensions(self):
        """Tests handling of invalid dimensions (negative values)."""
        with self.assertRaises(ValueError):
            sort(-100, 50, 30, 15)
        with self.assertRaises(ValueError):
            sort(100, -50, 30, 15)
        with self.assertRaises(ValueError):
            sort(100, 50, -30, 15)

    def test_invalid_mass(self):
        """Tests handling of invalid mass (negative value)."""
        with self.assertRaises(ValueError):
            sort(100, 50, 30, -15)

    def test_invalid_input_type(self):
        """Tests handling of invalid input types (strings)."""
        with self.assertRaises(TypeError):
            sort("invalid", 50, 30, 15)
        with self.assertRaises(TypeError):
            sort(100, "invalid", 30, 15)
        with self.assertRaises(TypeError):
            sort(100, 50, "invalid", 15)
        with self.assertRaises(TypeError):
            sort(100, 50, 30, "invalid")
