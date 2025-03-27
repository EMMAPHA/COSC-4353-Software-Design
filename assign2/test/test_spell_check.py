import unittest
from unittest.mock import patch
from src.spell_check import get_response, parse_response, is_spelling_correct

class SpellCheckTests(unittest.TestCase):
    def test_get_response_returns_value(self):
        self.assertTrue(len(get_response('hello')) > 0) 
        
    def test_parse_response_returns_true(self):
        self.assertTrue(parse_response('true'))

    def test_parse_response_returns_false(self):
        self.assertFalse(parse_response('false'))
    
    @patch('src.spell_check.parse_response', return_value = True)
    @patch('src.spell_check.get_response', return_value = 'true')
    def test_is_spelling_correct_true(self, mock_get_response, mock_parse_response):
        result = is_spelling_correct('hello')
        
        mock_get_response.assert_called_once_with('hello')   
        mock_parse_response.assert_called_once_with('true')
        self.assertTrue(result)
    
    @patch('src.spell_check.get_response')
    def test_is_spelling_correct_passes_exception(self, mock_get_response):
        mock_get_response.side_effect = Exception("Network Error")
        self.assertRaisesRegex(Exception, "Network Error", is_spelling_correct, 'hello')

if __name__ == '__main__':
    unittest.main()
    