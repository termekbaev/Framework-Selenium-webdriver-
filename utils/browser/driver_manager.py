from selenium.webdriver.remote.webdriver import WebDriver
from utils.config.config_reader import ConfigReader
from utils.browser.browser_factory import BrowserFactory
from utils.browser.singleton_meta import SingletonMeta
import logging

class DriverManager(metaclass=SingletonMeta):
    def __init__(self, config: ConfigReader) -> None:
        self._config = config
        self._driver = None
        self.logger = logging.getLogger(__name__)
        self._init_driver()

    @property
    def driver(self) -> WebDriver:
        if self._driver is None:
            self._init_driver()
        return self._driver

    def _init_driver(self) -> None:
        self.logger.info("Initializing driver...")
        try:
            self._driver = BrowserFactory(self._config).create_driver()
            self.logger.info(f"Driver started: {self._config.app_config.browser}")
        except Exception as e:
            self.logger.error(f"Driver initialization failed: {str(e)}")
            raise

    def quit(self) -> None:
        if self._driver is not None:
            self._driver.quit()
            self._driver = None