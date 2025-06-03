from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator, time=5, condition=EC.presence_of_element_located):
        return WebDriverWait(self.driver, time).until(condition(locator), 
                                                      f"Cant find element by locator '{locator}'"
                                                      )

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def is_element_displayed(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator), 
                                                      f"Cant find element by locator '{locator}'"
                                                      )
            return True
        except:
            return False
        
    def get_element_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text