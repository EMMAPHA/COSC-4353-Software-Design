import unittest
from src.blocks.z_blocker import z_blocker as zblock

class zblockerCharactersProcessorTests(unittest.TestCase):
    def test_z_blocker(self):
        self.assertEqual(zblock("z"), "")
        
    def test_z_blocker_with_any_other_character(self):
        self.assertEqual(zblock("a"), "a")
    
    def test_z_blocker_uppercase_Z(self):
        self.assertEqual(zblock("Z"), "Z")
    
    def test_z_blocker_non_letter_symbol(self):
        self.assertEqual(zblock("1"), "1")
        
if __name__ == '__main__':
    unittest.main()
