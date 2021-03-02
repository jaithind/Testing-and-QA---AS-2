import unittest
from savingCalc import savingCalc

class TestCase(unittest.TestCase):

    def test_savingCalc(self):
        result = savingCalc(25, 75000, 15, 100000)
        self.assertEqual(result, 32)