import json
from typing import List, Dict

class TestDataReader:
    def __init__(self, test_data_file):
        with open(test_data_file) as f:
            self.test_data = json.load(f)

    def get_users(self) -> List[Dict]:
        return self.test_data.get("users", [])