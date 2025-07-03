from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.browser.driver_manager import DriverManager
from typing import Tuple
import logging

class BasePage:
    def __init__(self, unique_element_locator: Tuple[By, str], check_is_opened=True) -> None:
        self.wait = WebDriverWait(DriverManager().driver, timeout=5)
        self.logger = logging.getLogger(__name__)
        self._unique_element_locator = unique_element_locator
        self.check_is_opened = check_is_opened
        
    def is_opened(self) -> bool:
        if self.wait.until(EC.visibility_of_element_located(self._unique_element_locator), 
                                f"Cant find element by locator '{self._unique_element_locator}'"
                                ).is_displayed() and self.check_is_opened:
            self.logger.info(f"Opened {self.__class__.__name__}")
            return True
        elif not self.check_is_opened:
            self.logger.info(f"Проверка открытия страницы отключена для {self.__class__.__name__}")
            return True
        return False