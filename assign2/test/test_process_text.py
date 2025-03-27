import unittest
import textwrap
from src.process_text import process_text

class ProcessTextTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)
    
    def test_empty_text(self):
        self.assertEqual(process_text(''), '')
        
    def test_process_hello(self):
        self.assertEqual(process_text('hello'), 'hello')
        
    def test_process_text_blah_which_we_will_consider_wrong_spelling(self):
        self.assertEqual(process_text('blah', lambda word: False), '[blah]')
    
    def test_process_hello_there(self):
        self.assertEqual(process_text("hello there", lambda word: word == "hello" or word == "there"), "hello there")
    
    def test_process_hello_tyop(self):
        self.assertEqual(process_text("hello tyop", lambda word: word != "tyop"), "hello [tyop]")
        
    def test_process_misp_hello(self):
        self.assertEqual(process_text("misp hello", lambda word: word != "misp"), "[misp] hello")
    
    def test_process_hello_tyop_there_misp(self):
        self.assertEqual(
            process_text("hello tyop there misp", lambda word: word != "tyop" and word != "misp"),
            "hello [tyop] there [misp]"
        )

    def test_process_text_with_two_lines(self):
        text = textwrap.dedent("""\
            hello world
            the cow""")
              
        self.assertEqual(
            process_text(text, lambda word: word in ["hello", "world", "the", "cow"]),
            textwrap.dedent("""\
                hello world
                the cow""")
        )

    def test_process_text_with_two_lines_some_incorrect(self):
        text = textwrap.dedent("""\
            hello wrld
            the caw""")
              
        self.assertEqual(
            process_text(text, lambda word: word in ["hello", "the"]),
            textwrap.dedent("""\
                hello [wrld]
                the [caw]""")
        )

    def test_process_text_with_three_lines(self):
        text = textwrap.dedent("""\
            hello world
            the cow
            jumps over""")
              
        self.assertEqual(
            process_text(text, lambda word: word in ["hello", "world", "the", "cow", "jumps", "over"]),
            textwrap.dedent("""\
                hello world
                the cow
                jumps over""")
        )

    def test_process_text_with_three_lines_some_incorrect(self):
        text = textwrap.dedent("""\
            hello wrld
            the cow
            jumps ovr""")
              
        self.assertEqual(
            process_text(text, lambda word: word in ["hello", "the", "cow", "jumps"]),
            textwrap.dedent("""\
                hello [wrld]
                the cow
                jumps [ovr]""")
        )
                                        
    def test_process_text_with_exception(self):
        text = "hello there how aare you"
    
        def spell_checker(word):
            if word == "there":
                raise Exception("Spell checker error")  
            
            return word != 'aare'
    
        self.assertEqual(process_text(text, spell_checker), "hello _there_ how [aare] you")  
    
if __name__ == "__main__":
    unittest.main()
