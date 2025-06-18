import json
from models.app_config import AppConfig

class ConfigReader:
    CONFIG_FILE_PATH = "config/config.json"

    def __init__(self, config_file_path: str = CONFIG_FILE_PATH) -> None:
        with open(config_file_path) as f:
            config_data = json.load(f)
            self.config = AppConfig(
                main_url=config_data["main_url"],
                browser=config_data.get("browser", "chrome"),
                chrome_options=config_data["chrome_options"],
                firefox_options=config_data["firefox_options"]
            )

    @property
    def app_config(self) -> AppConfig:
        return self.config