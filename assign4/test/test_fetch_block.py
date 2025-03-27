import unittest
from src.blocks.uppercase_converter import uppercase_converter
from src.blocks.lowercase_converter import lowercase_converter
from src.blocks.multiplier import multiplier
from src.blocks.Zblocker import Zblocker
from src.blocks.k_blocker import k_blocker
from src.blocks.z_blocker import z_blocker
from src.fetch_block import fetch_block

class TestFetchBlock(unittest.TestCase):

    def test_fetch_existing_block_uppercase(self):
        self.assertEqual(fetch_block("uppercase_converter"), uppercase_converter)
        
    def test_fetch_existing_block_lowercase(self):
        self.assertEqual(fetch_block("lowercase_converter"), lowercase_converter)

    def test_fetch_existing_block_multiplier(self):
        self.assertEqual(fetch_block("multiplier"), multiplier)

    def test_fetch_existing_block_Z_blocker(self):
        self.assertEqual(fetch_block("Zblocker"), Zblocker)

    def test_fetch_existing_block_k_blocker(self):
        self.assertEqual(fetch_block("k_blocker"), k_blocker)
        
    def test_fetch_existing_block_z_blocker(self):
        self.assertEqual(fetch_block("z_blocker"), z_blocker)
        
if __name__ == "__main__":
    unittest.main()
