import unittest
from src.crawler.github_api import GitHubAPI


class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        self.api = GitHubAPI()

    def test_fetch_directory(self):
        response = self.api.fetch_directory("https://api.github.com/repos/sgm1018/GitLLMTrainer/contents")
        self.assertIsInstance(response, list)

    def test_fetch_file_content(self):
        content = self.api.fetch_file_content("https://raw.githubusercontent.com/sgm1018/GitLLMTrainer/main/README.md")
        self.assertIsInstance(content, str)


if __name__ == "__main__":
    unittest.main()
