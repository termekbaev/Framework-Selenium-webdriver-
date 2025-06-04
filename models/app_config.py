from models.chrome_options_config import ChromeOptionsConfig
from models.firefox_options_config import FirefoxOptionsConfig

class AppConfig:
    def __init__(self, main_url: str, browser: str, chrome_options: dict, firefox_options: dict):
        self.main_url = main_url
        self.browser = browser.lower()
        self.chrome_options = ChromeOptionsConfig(**chrome_options)
        self.firefox_options = FirefoxOptionsConfig(**firefox_options)