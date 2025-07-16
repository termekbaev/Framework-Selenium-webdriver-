from selenium import webdriver
from utils.config.config_reader import ConfigReader
from typing import Union
import logging
import os

class BrowserFactory:
    def __init__(self, config: ConfigReader) -> None:
        self._config = config
        self.logger = logging.getLogger(__name__)

    def create_driver(self) -> Union[webdriver.Chrome, webdriver.Firefox]:
        browser_name = self._config.app_config.browser.lower()

        if browser_name == "chrome":
            return self._create_chrome_driver()
        elif browser_name == "firefox":
            return self._create_firefox_driver()
        raise ValueError(f"Unsupported browser: {browser_name}. Use 'chrome' or 'firefox'")

    def _create_chrome_driver(self) -> webdriver.Chrome:
        self.logger.info("Creating Chrome driver")
        try:
            options = webdriver.ChromeOptions()
            cfg = self._config.app_config.chrome_options
            test_name = os.environ.get('PYTEST_CURRENT_TEST')

            if "test_demoqa_files_uploading_and_downloading.py" in test_name:
                cfg.arguments.remove("--incognito")
                cfg.prefs["download.default_directory"] = r"C:\Users\t-erm\Downloads"
                options.add_experimental_option('prefs', cfg.prefs)

            for arg in cfg.arguments:
                options.add_argument(arg)
            options.page_load_strategy = cfg.page_load_strategy

            self.logger.info(f"With options = {cfg.__dict__}")

            driver = webdriver.Chrome(options=options)
            if "--headless=new" not in cfg.arguments:
                driver.maximize_window()
            return driver
        except Exception as e:
            self.logger.error(f"Chrome driver creation failed: {str(e)}")
            raise

    def _create_firefox_driver(self) -> webdriver.Firefox:
        self.logger.info("Creating Firefox driver")
        try:
            options = webdriver.FirefoxOptions()
            cfg = self._config.app_config.firefox_options
            test_name = os.environ.get('PYTEST_CURRENT_TEST')

            if "test_demoqa_files_uploading_and_downloading.py" in test_name:
                cfg.arguments.remove("--private")

            for arg in cfg.arguments:
                options.add_argument(arg)
                
            for pref, value in cfg.preferences.items():
                options.set_preference(pref, value)
            options.page_load_strategy = cfg.page_load_strategy

            self.logger.info(f"With options = {self._config.app_config.firefox_options.__dict__}")

            driver = webdriver.Firefox(options=options)
            driver.set_window_size(*map(int, cfg.window_size.split(',')))
            return driver
        except Exception as e:
            self.logger.error(f"Firefox driver creation failed: {str(e)}")
            raise