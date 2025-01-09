from config import GITHUB_API_URL
from crawler.github_api import GitHubAPI
from crawler.logger import get_logger
from crawler.json_formatter import JSONFormatter
from utils.helpers import is_valid_file


class GitHubScraper:
    def __init__(self, repo_url):
        self.api = GitHubAPI()
        self.repo_url = repo_url
        self.repo_api_url = self._convert_to_api_url(repo_url)
        self.data_tree = []
        self.logger = get_logger()

    def _convert_to_api_url(self, repo_url):
        """Convert a GitHub repository URL to the API equivalent."""
        parts = repo_url.rstrip("/").split("/")
        owner, repo = parts[-2], parts[-1]
        return f"{GITHUB_API_URL}/repos/{owner}/{repo}/contents"

    def scrape(self):
        """Start scraping the GitHub repository."""
        self.logger.info(f"Starting scraping for {self.repo_url}")
        self._scrape_directory(self.repo_api_url, "")
        self.logger.info(f"Scraping completed for {self.repo_url}")
        return self.data_tree

    def _scrape_directory(self, api_url, path_prefix):
        """Recursively scrape a directory."""
        contents = self.api.fetch_directory(api_url)
        for item in contents:
            if item["type"] == "file":
                content = self.api.fetch_file_content(item["download_url"]) if is_valid_file(item['name']) else ''
                self.data_tree.append({
                    "path": f"{path_prefix}/{item['name']}",
                    "type": "file",
                    "content": content
                })
                self.logger.info(f"File scraped: {item['path']}")
            elif item["type"] == "dir":
                self.logger.info(f"Entering directory: {item['path']}")
                self._scrape_directory(item["url"], f"{path_prefix}/{item['name']}")
