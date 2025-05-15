import os
import yaml

from chat_analysis.setup_logger import setup_logger

# Set up logging
logger = setup_logger("info")

def get_sentiment_key_words(path_to_txt_file: str) -> list[str]:
    """ 
    Extract key words from a .txt file. 
    Args:
        path_to_txt_file (str): path to the .txt file containing the key words
    Returns:
        key_words (list): list of key words
    """
    if not os.path.exists(path_to_txt_file):
        raise FileNotFoundError(f"Sentiment key words file not found: {path_to_txt_file}")

    with open(path_to_txt_file, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def get_chat_and_keywords_file_paths(config_path: str = 'chat_analysis/config.yaml') -> tuple[str, str]:
    """ 
    Get the chat and keywords file paths from the configuration file.
    Args:
        config (str, optional): path to the configuration file in yaml format. Defaults to 'chat_analysis/config.yaml'.
    Returns:
        chat_file_path (str): path to the chat file
        keywords_file_path (str): path to the keywords file
    """
    config = load_config(config_path)
    chat_file_path = os.path.join(config["root_path"], config["chat_example_file_path"])
    keywords_file_path = os.path.join(config["root_path"], config["sentiment_keywords_file_path"])
    return chat_file_path, keywords_file_path

def load_config(config_file: str) -> dict:
    """ 
    Load a configuration file in yaml format.
    Args:
        config_file (str): path to the configuration file in yaml format. 
    Returns:
        config (dict): dictionary containing the configuration
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config