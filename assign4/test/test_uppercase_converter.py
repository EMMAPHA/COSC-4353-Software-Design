import unittest
from src.blocks.uppercase_converter import uppercase_converter as uppercase

class UppercaseCharactersProcessorTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
        
    def test_lowercase_to_uppercase(self):
        self.assertEqual(uppercase("a"), "A")

    def test_uppercase_to_uppercase(self):
        self.assertEqual(uppercase("A"), "A")

    def test_uppercase_non_letter_symbol(self):
        self.assertEqual(uppercase("1"), "1")
 
if __name__ == '__main__':
    unittest.main()
