import unittest
from src.processor import process_text
from src.blocks.uppercase_converter import uppercase_converter
from src.blocks.lowercase_converter import lowercase_converter
from src.blocks.multiplier import multiplier
from src.blocks.z_blocker import z_blocker
from src.blocks.Zblocker import Zblocker
from src.blocks.k_blocker import k_blocker

class ProcessTextTests(unittest.TestCase):
    def test_no_blocks(self):
        self.assertEqual(process_text("hello"), "hello")

    def test_uppercase_block(self):
        self.assertEqual(process_text("hello", uppercase_converter), "HELLO") 

    def test_z_blocker(self):
        self.assertEqual(process_text("zebra", z_blocker), "ebra")
    
    def test_k_blocker(self):
        self.assertEqual(process_text("kite", k_blocker), "ite")
        
    def test_multiplier_block(self):
        self.assertEqual(process_text("a", multiplier), "aa")
        
    def test_multiple_blocks(self):
        self.assertEqual(process_text("ZHello", uppercase_converter, Zblocker, lowercase_converter), "hello")
        
    def test_abzde_uppercase_and_Z_blocker(self):
        self.assertEqual(process_text("abzde", uppercase_converter, Zblocker), "ABDE")

    def test_abzde_Z_blocker_and_uppercase(self):
        self.assertEqual(process_text("abzde", Zblocker, uppercase_converter), "ABZDE")

    def test_abzde_uppercase_and_multiplier(self):
        self.assertEqual(process_text("abzde", uppercase_converter, multiplier), "AABBZZDDEE")

    def test_abzde_Z_blocker_uppercase_and_multiplier(self):
        self.assertEqual(process_text("abzde", Zblocker, uppercase_converter, multiplier), "AABBZZDDEE")
        
if __name__ == '__main__':
    unittest.main()
    