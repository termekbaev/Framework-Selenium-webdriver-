from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class FrameUtil:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def switch_to_frame(self, frame_locator):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame_locator))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def is_frame_available(self, frame_locator):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
            self.driver.switch_to.default_content()
            return True
        except TimeoutException:
            return False