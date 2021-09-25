import pytest
from pytest_django.asserts import TestCase
from .calc import add, substract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Tests that two numbers are added together"""
        self.assertEqual(add(3,8), 11)
        
    
    def test_substract_numbers(self):
        """Tests that values are substracted and returned"""
        self.assertEqual(substract(11,5), 6)