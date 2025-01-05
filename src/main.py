import sys
from crawler.scraper import GitHubScraper
from crawler.json_formatter import JSONFormatter
from utils.helpers import is_valid_url
from crawler.logger import get_logger, print_hero

logger = get_logger()

def main():
    if len(sys.argv) < 2:
        logger.error("Usage: python main.py <GitHub repository URL>")
        sys.exit(1)

    repo_url = sys.argv[1]
    if not is_valid_url(repo_url):
        logger.error("Invalid GitHub URL. Please provide a valid URL.")
        sys.exit(1)


    print_hero()
    scraper = GitHubScraper(repo_url)
    data = scraper.scrape()

    output_file = "repo_data.json"
    JSONFormatter.save_to_file(data, output_file)
    logger.info(f"Data saved to {output_file}")


if __name__ == "__main__":
    main()
