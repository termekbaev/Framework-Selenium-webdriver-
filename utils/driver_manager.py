from utils.config_reader import ConfigReader
from utils.browser_factory import BrowserFactory

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DriverManager(metaclass=SingletonMeta):
    def __init__(self, config: ConfigReader):
        self._config = config
        self._driver = None

    @property
    def driver(self):
        if self._driver is None:
            self._init_driver()
        return self._driver

    def _init_driver(self):
        self._driver = BrowserFactory(self._config).create_driver()

    def quit(self):
        if self._driver is not None:
            self._driver.quit()
            self._driver = None