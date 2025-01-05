import requests
import sys
sys.path.append('..')
from config import GITHUB_API_URL, GITHUB_TOKEN
import time


class GitHubAPI:
    def __init__(self):
        self.headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

    def fetch_directory(self, url):
        """Fetch the contents of a directory from the GitHub API."""
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        time.sleep(0.3)
        return response.json()

    def fetch_file_content(self, download_url):
        """Fetch the raw content of a file."""
        response = requests.get(download_url, headers=self.headers)
        response.raise_for_status()
        time.sleep(0.3)
        return response.text
