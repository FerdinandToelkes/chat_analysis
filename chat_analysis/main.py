from chat_analysis.chat_analyzer import ChatAnalyzer
from chat_analysis.utils import get_chat_and_keywords_file_paths
from chat_analysis.setup_logger import setup_logger

# Set up logging
logger = setup_logger("debug")


if __name__ == "__main__":
    chat_file_path, keywords_file_path = get_chat_and_keywords_file_paths()
    chat_analyzer = ChatAnalyzer(chat_file_path, keywords_file_path)
    logger.debug("Starting ChatAnalyzer script...")
    stats = chat_analyzer.get_basic_chat_info()
    logger.debug(f"Chat statistics: {stats}")
    sentiment = chat_analyzer.get_chat_sentiment()
    logger.debug(f"Chat sentiment: {sentiment}")

    print(chat_analyzer.chat)
    chat_analyzer.print_responses(chat_analyzer.name_one)

    print(stats)
