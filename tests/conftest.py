import pytest
import logging
import os
from utils.config_reader import ConfigReader
from utils.driver_manager import DriverManager
from utils.data_reader import TestDataReader

_log_file_cleared = False

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
def setup_logging(request):
    global _log_file_cleared

    if not _log_file_cleared:
        with open("test.log", "w") as f:
            f.write("")
        _log_file_cleared = True

    test_file = os.path.basename(request.node.fspath.strpath)
    logger = logging.getLogger(request.node.nodeid)

    if not logger.handlers:
        with open("test.log", "a") as f:
            f.write(f"\n======= Test {test_file} starts =======\n")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.FileHandler("test.log", "a"),
            logging.StreamHandler()
        ],
        force=True
    )

    yield logger

    logging.info(f"Test {request.node.nodeid} completed")