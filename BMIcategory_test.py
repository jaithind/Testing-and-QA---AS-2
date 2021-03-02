import unittest
from BMIcategory import BMIcategory

class TestCase(unittest.TestCase):
    
    def test_BMIcalc(self):
        result = BMIcategory('14')
        self.assertTrue(result, "Underweight")
        
    def test_BMIcalc(self):
        result = BMIcategory('20')
        self.assertTrue(result, "Normal Weight")
        
    def test_BMIcalc(self):
        result = BMIcategory('25')
        self.assertTrue(result, "Overweight")
        
    def test_BMIcalc(self):
        result = BMIcategory('35')
        self.assertTrue(result, "Obese")