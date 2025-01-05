import logging
from colorlog import ColoredFormatter


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
