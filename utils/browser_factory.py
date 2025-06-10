from selenium import webdriver
from utils.config_reader import ConfigReader
from utils.logger import Logger
from typing import Union
import logging

class BrowserFactory:
    CHROME_HEADLESS = "--headless=new"
    CHROME_INCOGNITO = "--incognito"
    CHROME_DISABLE_EXTENSIONS = "--disable-extensions"
    CHROME_LANG = "--lang={}"
    CHROME_WINDOW_SIZE = "--window-size={}"

    FIREFOX_HEADLESS = "--headless"
    FIREFOX_PRIVATE = "--private"
    FIREFOX_DISABLE_EXTENSIONS = "--disable-extensions"
    FIREFOX_LANG_PREFERENCE = "intl.accept_languages"

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

            if cfg.headless:
                options.add_argument(self.CHROME_HEADLESS)
            if cfg.incognito:
                options.add_argument(self.CHROME_INCOGNITO)
            if cfg.disable_extensions:
                options.add_argument(self.CHROME_DISABLE_EXTENSIONS)

            options.add_argument(self.CHROME_LANG.format(cfg.lang))
            options.add_argument(self.CHROME_WINDOW_SIZE.format(cfg.window_size))
            options.page_load_strategy = cfg.page_load_strategy

            self.logger.info(f"With options = {self._config.app_config.chrome_options.__dict__}")

            driver = webdriver.Chrome(options=options)
            if not cfg.headless:
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

            if cfg.headless:
                options.add_argument(self.FIREFOX_HEADLESS)
            if cfg.private:
                options.add_argument(self.FIREFOX_PRIVATE)
            if cfg.disable_extensions:
                options.add_argument(self.FIREFOX_DISABLE_EXTENSIONS)

            options.set_preference(self.FIREFOX_LANG_PREFERENCE, cfg.lang)
            options.page_load_strategy = cfg.page_load_strategy

            self.logger.info(f"With options = {self._config.app_config.firefox_options.__dict__}")

            driver = webdriver.Firefox(options=options)
            driver.set_window_size(*map(int, cfg.window_size.split(',')))
            return driver
        except Exception as e:
            self.logger.error(f"Firefox driver creation failed: {str(e)}")
            raise