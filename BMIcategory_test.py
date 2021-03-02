import unittest
from BMIcategory import BMIcategory

class TestCase(unittest.TestCase):
    
    def test_BMIcalc(self):
        result = BMIcategory(14)
        self.assertEqual(result, "Underweight")
        
    def test_BMIcalc2(self):
        result = BMIcategory(20)
        self.assertEqual(result, "Normal Weight")
        
    def test_BMIcalc3(self):
        result = BMIcategory(25)
        self.assertEqual(result, "Overweight")
        
    def test_BMIcalc4(self):
        result = BMIcategory(35)
        self.assertEqual(result, "Obese")