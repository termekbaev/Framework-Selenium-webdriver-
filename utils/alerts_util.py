from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoAlertPresentException

class AlertUtil:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def is_alert_present(self) -> bool:
        try:
            WebDriverWait(self.driver, 1).until(EC.alert_is_present())
            return True
        except:
            return False

    def get_alert_text(self) -> str:
        if not self.is_alert_present():
            raise NoAlertPresentException("Alert not present")
        alert = self.driver.switch_to.alert
        return alert.text
        
    def accept_alert(self) -> None:
        if not self.is_alert_present():
            raise NoAlertPresentException("Alert not present")
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self) -> None:
        if not self.is_alert_present():
            raise NoAlertPresentException("Alert not present")
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def send_text_to_alert(self, text: str) -> None:
        if not self.is_alert_present():
            raise NoAlertPresentException("Alert not present")
        alert = self.driver.switch_to.alert
        alert.send_keys(text)