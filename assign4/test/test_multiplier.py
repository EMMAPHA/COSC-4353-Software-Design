import unittest
from src.blocks.multiplier import multiplier

class MultiplierCharactersProcessorTests(unittest.TestCase):
    def test_single_character_multiplier(self):
        self.assertEqual(multiplier("a"), "aa")

    def test_multiplier_non_letter_symbol(self):
        self.assertEqual(multiplier("1"), "11")
 
if __name__ == '__main__':
    unittest.main()
  