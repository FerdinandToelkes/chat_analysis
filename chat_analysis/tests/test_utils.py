import unittest
import os
from chat_analysis.utils import get_sentiment_key_words

class TestUtils(unittest.TestCase):
    """Test the utility functions in utils.py"""
    def setUp(self):
        """Create a temporary file with some key words for testing before each test"""
        self.test_file_path = '/tmp/test_sentiment_keywords.txt'
        with open(self.test_file_path, 'w', encoding='utf-8') as f:
            f.write("sympathy\njoy\nnegative_emotion\ncheerfulness\n")

    def tearDown(self):
        """Remove the temporary file after tests"""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_get_sentiment_key_words(self):
        """Test if key words are extracted correctly from a file"""
        expected_keywords = ['sympathy', 'joy', 'negative_emotion', 'cheerfulness']
        result = get_sentiment_key_words(self.test_file_path)
        self.assertEqual(result, expected_keywords)

    def test_get_sentiment_key_words_file_not_found(self):
        """Test if FileNotFoundError is raised when the file is not found"""
        with self.assertRaises(FileNotFoundError):
            get_sentiment_key_words('/path/to/nonexistent/file.txt')

if __name__ == '__main__':
    unittest.main()