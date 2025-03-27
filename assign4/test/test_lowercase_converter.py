import unittest
from src.blocks.lowercase_converter import lowercase_converter as lowercase

class LowercaseCharactersProcessorTests(unittest.TestCase):       
    def test_uppercase_to_lowercase(self):
        self.assertEqual(lowercase("B"), "b")
    
    def test_lowercase_to_lowercase(self):
        self.assertEqual(lowercase("b"), "b")

    def test_lowercase_non_letter_symbol(self):
        self.assertEqual(lowercase("1"), "1")
 
if __name__ == '__main__':
    unittest.main()
    