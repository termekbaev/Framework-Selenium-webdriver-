import json
from typing import List, Dict

class DataReader:
    def __init__(self, test_data_file: str) -> None:
        with open(test_data_file) as f:
            self.test_data = json.load(f)

    def get_users(self) -> List[Dict[str, str]]:
        return self.test_data.get("users", [])
    
    def get_alert_texts(self) -> Dict[str, str]:
        return {
            "alert_text": self.test_data.get("alert_text"),
            "confirm_text": self.test_data.get("confirm_text"),
            "confirm_result": self.test_data.get("confirm_result"),
            "prompt_text": self.test_data.get("prompt_text"),
            "prompt_result_prefix": self.test_data.get("prompt_result_prefix")
        }