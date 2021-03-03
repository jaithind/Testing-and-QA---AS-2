import unittest
from unittest.mock import patch
from getPosValue import getPosValue

class TestCase(unittest.TestCase):
    
    @patch('builtins.input', return_value = "100")
    def test_posValue_100(self, mockinput):
        result = getPosValue("Test")
        self.assertEqual(result, 100)
        