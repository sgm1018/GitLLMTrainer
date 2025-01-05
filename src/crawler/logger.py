import logging
from colorlog import ColoredFormatter


def print_hero():
    """Print the hero section of the program."""
    hero_text = """
    \033[1;32m

   ____ _ _   _     _     __  __ _____          _                 
  / ___(_) |_| |   | |   |  \/  |_   _| __ __ _(_)_ __   ___ _ __ 
 | |  _| | __| |   | |   | |\/| | | || '__/ _` | | '_ \ / _ \ '__|
 | |_| | | |_| |___| |___| |  | | | || | | (_| | | | | |  __/ |   
  \____|_|\__|_____|_____|_|  |_| |_||_|  \__,_|_|_| |_|\___|_|   
                                                                  
    \033[0m
    \033[1;34m
    GitLLMTrainer - A tool to train and fine-tune language models on GitHub repositories.
    \033[0m
    \033[1;36m
    Repository: https://github.com/sgm1018/GitLLMTrainer
    \033[0m
    """
    print(hero_text)

    warning_text = """
    \033[1;33m
    [WARNING] The developers of this program are not responsible for any malicious use of this tool. 
    This program is intended for educational purposes only. Use it responsibly and in accordance with 
    applicable laws and regulations.
    \033[0m
    """
    print(warning_text)

def get_logger():
    """Create a logger with colored output."""
    logger = logging.getLogger("GitHubScraper")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter(
        "%(log_color)s[%(levelname)s] %(message)s",
        log_colors={
            "INFO": "cyan",
            "WARNING": "yellow",
            "ERROR": "red",
            "DEBUG": "blue"
        }
    ))
    logger.addHandler(handler)
    return logger
