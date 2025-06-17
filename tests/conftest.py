from utils.config_reader import ConfigReader
from utils.driver_manager import DriverManager
from utils.data_reader import TestDataReader
from utils.logger import Logger
from typing import Generator
import pytest
import logging


@pytest.fixture(autouse=True)
def setup_driver(config: ConfigReader) -> Generator[None, None, None]:
    DriverManager(config).driver.get(config.app_config.main_url)
    yield
    DriverManager().quit()

@pytest.fixture
def config() -> ConfigReader:
    return ConfigReader()

@pytest.fixture
def web_tables_test_data() -> TestDataReader:
    return TestDataReader("config/test_web_tables_data.json")

@pytest.fixture(autouse=True)
def setup_logging(request: pytest.FixtureRequest) -> Generator[logging.Logger, None, None]:
    yield from Logger.setup_logging(request)