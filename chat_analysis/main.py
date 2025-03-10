import logging
from chat_analysis.chat_analyzer import ChatAnalyzer
from chat_analysis.utils import get_chat_and_keywords_file_paths

# Configure logging at the module level
logging.basicConfig(
    level=logging.DEBUG, 
    format="%(name)s - %(asctime)s - %(levelname)s - %(message)s"
)

# Get the logger for this script (one logger per module)
logger = logging.getLogger(__name__)  


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
