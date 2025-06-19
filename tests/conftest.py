from utils.config.config_reader import ConfigReader
from utils.config.data_reader import DataReader
from utils.browser.driver_manager import DriverManager
from utils.logging.logger import Logger
from typing import Generator
import pytest
import logging


@pytest.fixture(autouse=True)
def setup_driver(config: ConfigReader, setup_logging) -> Generator[None, None, None]:
    driver_manager = DriverManager(config)
    driver = driver_manager.driver
    driver.get(config.app_config.main_url)
    yield
    driver_manager.quit()

@pytest.fixture
def config() -> ConfigReader:
    return ConfigReader()

@pytest.fixture
def alerts_test_data() -> DataReader:
    return DataReader("config/test_alerts_data.json")

@pytest.fixture
def frames_test_data() -> DataReader:
    return DataReader("config/test_frames_data.json")

@pytest.fixture(autouse=True)
def setup_logging(request: pytest.FixtureRequest) -> Generator[logging.Logger, None, None]:
    yield from Logger.setup_logging(request)