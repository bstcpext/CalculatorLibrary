#!/bin/bash
"""
Unit tests for the calculator library
"""

import unittest
import mycalculator


class TestMyCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(mycalculator.add(2, 2), 4)

    def test_subtraction(self):
        self.assertEqual(mycalculator.subtract(4, 2), 2)

    def test_multiplication(self):
        self.assertEqual(mycalculator.multiply(10, 10), 100)

    def test_division(self):
        self.assertEqual(mycalculator.divide(100, 20), 5)
