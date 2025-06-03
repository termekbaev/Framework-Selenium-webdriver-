from models.chrome_options_config import ChromeOptionsConfig

class AppConfig:
    def __init__(self, main_url: str, chrome_options: dict):
        self.main_url = main_url
        self.chrome_options = ChromeOptionsConfig(**chrome_options)