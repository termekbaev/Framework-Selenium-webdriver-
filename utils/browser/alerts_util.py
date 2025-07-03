from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from utils.browser.driver_manager import DriverManager
import logging
import random
import string

class AlertUtil:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def is_alert_present(self) -> bool:
        try:
            WebDriverWait(DriverManager().driver, 1).until(EC.alert_is_present())
            return True
        except:
            return False

    def get_alert_text(self) -> str:
        if not self.is_alert_present():
            raise NoAlertPresentException("Alert not present")
        alert = DriverManager().driver.switch_to.alert
        self.logger.info(f"Get alert text '{alert.text}'")
        return alert.text
        
    def accept_alert(self) -> None:
        if not self.is_alert_present():
            raise NoAlertPresentException("Alert not present")
        alert = DriverManager().driver.switch_to.alert
        alert.accept()
        self.logger.info(f"Alert accepted")

    def dismiss_alert(self) -> None:
        if not self.is_alert_present():
            raise NoAlertPresentException("Alert not present")
        alert = DriverManager().driver.switch_to.alert
        alert.dismiss()
        self.logger.info(f"Alert dismissed")

    def send_text_to_alert(self, text: str) -> None:
        if not self.is_alert_present():
            raise NoAlertPresentException("Alert not present")
        alert = DriverManager().driver.switch_to.alert
        alert.send_keys(text)
        self.logger.info(f"Sended text '{text}' to alert")

    def generate_random_text(self, length: int = 20) -> str:
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))