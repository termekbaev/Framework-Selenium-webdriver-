from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
import logging

class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=5)
        self.logger = logging.getLogger(__name__)
        
    def is_opened(self) -> bool:
        if self.wait.until(EC.visibility_of_element_located(self.UNIQUE_ELEMENT), 
                                f"Cant find element by locator '{self.UNIQUE_ELEMENT}'"
                                ).is_displayed():
            self.logger.info(f"Opened {self.__class__.__name__}")
            return True
        return False