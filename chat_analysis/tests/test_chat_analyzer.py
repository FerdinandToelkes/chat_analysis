import unittest
from chat_analysis.chat_analyzer import ChatAnalyzer


class TestChatAnalyzer(unittest.TestCase):
    def setUp(self):
        """Runs before each test. Useful for setting up test data."""
        self.analyzer = ChatAnalyzer("Replika_Chat_Test.docx")

    def test_extract_names(self):
        """Test if names are extracted correctly"""
        self.assertEqual(self.analyzer.name_one, "Alex")
        self.assertEqual(self.analyzer.name_two, "you")

    def test_get_basic_chat_info(self):
        """Test chat statistics calculation"""
        stats = self.analyzer.get_basic_chat_info()
        self.assertIsInstance(stats, dict)
        self.assertIn("name_one", stats)
        self.assertIn("name_two", stats)
        self.assertIn("number_of_responses_name_one", stats)
        self.assertIn("number_of_responses_name_two", stats)
        self.assertIn("total_number_of_seperate_texts", stats)
        self.assertIn("total_number_of_words_name_one", stats)
        self.assertIn("total_number_of_words_name_two", stats)
        self.assertIn("total_number_of_words", stats)
        # Check if these numbers match with the humanly calculated numbers
        #TODO

    def test_extract_conversation_parts(self):
        """Check if conversation parts are extracted correctly"""
        chat = self.analyzer.extract_conversation_parts()
        self.assertIsInstance(chat, dict)
        # Check if there are exactly two keys in the chat dictionary
        self.assertEqual(len(chat), 2)
        # Check if both names are in the chat keys
        self.assertIn(self.analyzer.name_one, chat)
        self.assertIn(self.analyzer.name_two, chat)

if __name__ == "__main__":
    unittest.main()
