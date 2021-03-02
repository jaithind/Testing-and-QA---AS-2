import unittest
from BMIcalc import BMIcalc

class TestCase(unittest.TestCase):
        
    def test_BMIcalc(self):
        result = BMIcalc(6, 2, 150)
        self.assertEqual(result, 19.7)
        
    def test_BMIcalc2(self):
        result = BMIcalc(5, 3, 125)
        self.assertEqual(result, 22.7)
        
        