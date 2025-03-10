import logging
from chat_analysis.chat_analyzer import ChatAnalyzer

# Configure logging at the module level
logging.basicConfig(
    level=logging.INFO, 
    format="%(name)s - %(asctime)s - %(levelname)s - %(message)s"
)

# Get the logger for this script (one logger per module)
logger = logging.getLogger(__name__)  


if __name__ == "__main__":
    path = "ID 1.docx"
    chat_analyzer = ChatAnalyzer(path)
    logger.info("Starting ChatAnalyzer script...")
    stats = chat_analyzer.get_basic_chat_info()
    logger.info(f"Chat statistics: {stats}")
    sentiment = chat_analyzer.get_chat_sentiment()
    logger.info(f"Chat sentiment: {sentiment}")

    print(chat_analyzer.chat)
    chat_analyzer.print_responses(chat_analyzer.name_one)

    print(stats)
