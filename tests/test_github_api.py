import unittest
from src.crawler.github_api import GitHubAPI


class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        self.api = GitHubAPI()

    def test_fetch_directory(self):
        response = self.api.fetch_directory("https://api.github.com/repos/tldraw/tldraw/contents")
        self.assertIsInstance(response, list)

    def test_fetch_file_content(self):
        content = self.api.fetch_file_content("https://raw.githubusercontent.com/tldraw/tldraw/main/.dockerignore")
        self.assertIsInstance(content, str)


if __name__ == "__main__":
    unittest.main()
