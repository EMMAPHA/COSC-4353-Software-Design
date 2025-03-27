import unittest
from src.blocks.Zblocker import Zblocker as Zblock

class ZblockerCharactersProcessorTests(unittest.TestCase):
    def test_Z_blocker_uppercase_Z(self):
        self.assertEqual(Zblock("Z"), "")
        
    def test_Z_blocker_with_any_other_character(self):
        self.assertEqual(Zblock("b"), "b")
        
    def test_Z_blocker_lowercase_z(self):
        self.assertEqual(Zblock("z"), "z")

    def test_Z_blocker_non_letter_symbol(self):
        self.assertEqual(Zblock("2"), "2")
        
if __name__ == '__main__':
    unittest.main()
