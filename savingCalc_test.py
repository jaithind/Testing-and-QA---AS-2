# To execute this test file type the following in a ternmainal: 
# python -m unittest savingCalc_test.py

import unittest
from savingCalc import savingCalc

class TestCase(unittest.TestCase):

    def test_savingCalc(self):
        result = savingCalc(25, 75000, 15, 100000)
        self.assertEqual(result, 32)
        
    def test_savingCalc_100plus(self):
        result = savingCalc(65, 35000, 5, 100000)
        self.assertEqual(result, 107)