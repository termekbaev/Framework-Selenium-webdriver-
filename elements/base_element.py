from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.browser.driver_manager import DriverManager
from typing import Tuple, List
import logging

class BaseElement:
    def __init__(self, 
                 locator: Tuple[By, str], 
                 name: str = "", 
                 timeout: int = 5
    ) -> None:
        self.locator = locator
        self.name = name
        self.timeout = timeout
        self.driver = DriverManager().driver
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.logger = logging.getLogger(__name__)

    def find_element(self) -> WebElement:
        return self.wait.until(
            EC.visibility_of_element_located(self.locator),
            f"Element '{self.name} = {self.locator}' not found!"
        )
    
    def find_elements(self) -> List[WebElement]:
        return self.wait.until(
            EC.visibility_of_any_elements_located(self.locator),
            f"No elements found by locator '{self.locator}'"
        )

    def is_displayed(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.locator), 
                            f"Cant find element by locator '{self.locator}'"
                            )
            return True
        except:
            return False