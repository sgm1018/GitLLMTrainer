import json


class JSONFormatter:
    @staticmethod
    def save_to_file(data, output_path):
        """Save data to a JSON file."""
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
