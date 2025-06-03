from utils.config_reader import ConfigReader
from selenium import webdriver

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DriverManager(metaclass=SingletonMeta):
    CHROME_HEADLESS = "--headless=new"
    CHROME_INCOGNITO = "--incognito"
    CHROME_DISABLE_EXTENSIONS = "--disable-extensions"
    CHROME_LANG_TEMPLATE = "--lang={}"
    CHROME_WINDOW_SIZE_TEMPLATE = "--window-size={}"
    CHROME_PAGE_LOAD_STRATEGY = "{}"

    def __init__(self, config: ConfigReader):
        self._config = config
        self._driver = None

    @property
    def driver(self):
        if self._driver is None:
            self._init_driver()
        return self._driver

    def _init_driver(self):
        options = webdriver.ChromeOptions()

        if self._config.app_config.chrome_options.headless:
            options.add_argument(self.CHROME_HEADLESS)
        if self._config.app_config.chrome_options.incognito:
            options.add_argument(self.CHROME_INCOGNITO)
        if self._config.app_config.chrome_options.disable_extensions:
            options.add_argument(self.CHROME_DISABLE_EXTENSIONS)
        options.add_argument(self.CHROME_LANG_TEMPLATE.format(self._config.app_config.chrome_options.lang))
        options.add_argument(self.CHROME_WINDOW_SIZE_TEMPLATE.format(self._config.app_config.chrome_options.window_size))
        options.page_load_strategy = self.CHROME_PAGE_LOAD_STRATEGY.format(self._config.app_config.chrome_options.page_load_strategy)
        for arg in self._config.app_config.chrome_options.additional_args:
            options.add_argument(arg)

        self._driver = webdriver.Chrome(options=options)
        self._driver.maximize_window()

    def quit(self):
        if self._driver is not None:
            self._driver.quit()
            self._driver = None