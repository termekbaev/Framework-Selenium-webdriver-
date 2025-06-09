from selenium.webdriver.remote.webdriver import WebDriver
from utils.config_reader import ConfigReader
from utils.browser_factory import BrowserFactory
from utils.singleton_meta import SingletonMeta

class DriverManager(metaclass=SingletonMeta):
    def __init__(self, config: ConfigReader) -> None:
        self._config = config
        self._driver = None

    @property
    def driver(self) -> WebDriver:
        if self._driver is None:
            self._init_driver()
        return self._driver

    def _init_driver(self) -> None:
        self._driver = BrowserFactory(self._config).create_driver()

    def quit(self) -> None:
        if self._driver is not None:
            self._driver.quit()
            self._driver = None