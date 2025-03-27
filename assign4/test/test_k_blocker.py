import unittest
from src.blocks.k_blocker import k_blocker as kblock

class kblockerCharactersProcessorTests(unittest.TestCase):
    def test_k_blocker(self):
        self.assertEqual(kblock("k"), "")
        
    def test_k_blocker_with_any_other_character(self):
        self.assertEqual(kblock("apple"), "apple")
        
    def test_k_blocker_uppercase_K(self):
        self.assertEqual(kblock("K"), "K")
        
    def test_k_blocker_non_letter_symbol(self):
        self.assertEqual(kblock("3"), "3")
         
if __name__ == '__main__':
    unittest.main()
    