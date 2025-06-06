from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
import string

class AlertsPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, "javascriptAlertsWrapper")
    ALERT_BUTTON = (By.ID, "alertButton")
    CONFIRM_BUTTON = (By.ID, "confirmButton")
    PROMPT_BUTTON = (By.ID, "promtButton")
    CONFIRM_RESULT = (By.ID, "confirmResult")
    PROMPT_RESULT = (By.ID, "promptResult")

    def generate_random_text(self, length=20):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def get_alert_message_and_accept(self):
        if self.is_alert_presented():
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        else:
            raise TimeoutException("Alert not presented")

    def get_confirm_message_and_confirm_result_message(self):
        if self.is_alert_presented():
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept() 
            return alert_text, self.find_element(self.CONFIRM_RESULT).text
        else:
            raise TimeoutException("Alert not presented")

    def get_prompt_message_and_prompt_result_message(self):
        if self.is_alert_presented():
            random_text = self.generate_random_text()
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.send_keys(random_text)
            alert.accept()
            return random_text, alert_text, self.find_element(self.PROMPT_RESULT).text
        else:
            raise TimeoutException("Alert not presented")