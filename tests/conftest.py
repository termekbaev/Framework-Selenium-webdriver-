import pytest
import logging
from utils.config_reader import ConfigReader
from utils.driver_manager import DriverManager
from utils.data_reader import TestDataReader

@pytest.fixture()
def driver_manager(config):
    driver_manager = DriverManager(config)
    yield driver_manager
    driver_manager.quit()

@pytest.fixture
def config():
    return ConfigReader()

@pytest.fixture
def alerts_test_data():
    return TestDataReader("config/test_alerts_data.json")

@pytest.fixture(autouse=True)
def setup_logging():
    with open('test.log', 'w') as f:
        f.write("=== НАЧАЛО ТЕСТИРОВАНИЯ ===\n")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%H:%M:%S',
        handlers=[
            logging.FileHandler('test.log', 'a'),
            logging.StreamHandler()
        ],
        force=True
    )