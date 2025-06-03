import json

class TestDataReader:
    def __init__(self, test_data_file):
        with open(test_data_file) as f:
            self.test_data = json.load(f)