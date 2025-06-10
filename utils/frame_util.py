from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple
import logging

class FrameUtil:
    def __init__(self, driver: WebDriver, timeout: int = 5) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = logging.getLogger(__name__)

    def switch_to_frame(self, frame_locator: Tuple[By, str]) -> None:
        self.logger.info(f"Switching to frame: {frame_locator}")
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
        except TimeoutException:
            self.logger.error(f"Frame not available: {frame_locator}")
            raise

    def switch_to_default_content(self) -> None:
        self.logger.info(f"Switching to default content")
        self.driver.switch_to.default_content()

    def is_frame_available(self, frame_locator: Tuple[By, str]) -> bool:
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
            self.driver.switch_to.default_content()
            return True
        except TimeoutException:
            return False