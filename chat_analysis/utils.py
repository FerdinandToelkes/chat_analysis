import os


def get_sentiment_key_words(path_to_txt_file: str) -> list[str]:
    """ Extract key words from a .txt file. 
    Args:
        path_to_txt_file (str): path to the .txt file containing the key words
    
    Returns:
        key_words (list): list of key words"""
    if not os.path.exists(path_to_txt_file):
        raise FileNotFoundError(f"Sentiment key words file not found: {path_to_txt_file}")

    with open(path_to_txt_file, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
