import unittest
import os
from chat_analysis.utils import get_sentiment_key_words, get_chat_and_keywords_file_paths

class TestUtils(unittest.TestCase):
    """Test the utility functions in utils.py"""
    def setUp(self):
        """Create a temporary file with some key words and a configuration
        file for testing"""
        self.test_keywords_file_path = '/tmp/test_sentiment_keywords.txt'
        self.test_config_file_path = '/tmp/test_config.yaml'

        with open(self.test_keywords_file_path, 'w', encoding='utf-8') as f:
            f.write("sympathy\njoy\nnegative_emotion\ncheerfulness\n")

        with open(self.test_config_file_path, 'w', encoding='utf-8') as f:
            f.write("root_path: /tmp\nchat_example_file_path: chat_example.docx\nsentiment_keywords_file_path: test_sentiment_keywords.txt\n")

    def tearDown(self):
        """Remove the temporary files after tests"""
        if os.path.exists(self.test_keywords_file_path):
            os.remove(self.test_keywords_file_path)
        if os.path.exists(self.test_config_file_path):
            os.remove(self.test_config_file_path)

    def test_get_sentiment_key_words(self):
        """Test if key words are extracted correctly from a file"""
        expected_keywords = ['sympathy', 'joy', 'negative_emotion', 'cheerfulness']
        result = get_sentiment_key_words(self.test_keywords_file_path)
        self.assertEqual(result, expected_keywords)

    def test_get_sentiment_key_words_file_not_found(self):
        """Test if FileNotFoundError is raised when the file is not found"""
        with self.assertRaises(FileNotFoundError):
            get_sentiment_key_words('/path/to/nonexistent/file.txt')

    def test_get_chat_and_keywords_file_paths(self):
        """Test if chat and keywords file paths are extracted correctly from a configuration file"""
        chat_file_path, keywords_file_path = get_chat_and_keywords_file_paths(self.test_config_file_path)
        self.assertEqual(chat_file_path, '/tmp/chat_example.docx')
        self.assertEqual(keywords_file_path, '/tmp/test_sentiment_keywords.txt')

if __name__ == '__main__':
    unittest.main()