from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
import string

class AlertsPage(BasePage):
    GO_TO_ALERTS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-1']")
    ALERTS_SECTION = (By.ID, "javascriptAlertsWrapper")
    ALERT_BUTTON = (By.ID, "alertButton")
    CONFIRM_BUTTON = (By.ID, "confirmButton")
    PROMPT_BUTTON = (By.ID, "promtButton")
    CONFIRM_RESULT = (By.ID, "confirmResult")
    PROMPT_RESULT = (By.ID, "promptResult")


    def generate_random_text(self, length=8):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def open_alerts_section(self):
        self.click(self.GO_TO_ALERTS_SECTION)
    
    def is_opened_alerts_section(self):
        return self.is_element_displayed(self.ALERTS_SECTION)
    
    def is_alert_presented(self):
        try:
            WebDriverWait(self.driver, 1).until(EC.alert_is_present())
            return True
        except:
            return False

    def check_alert_message_then_accept(self):
        if self.is_alert_presented():
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        else:
            raise TimeoutException("Alert not presented")

    def handle_confirm(self):
        if self.is_alert_presented():
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept() 
            return alert_text, self.find_element(self.CONFIRM_RESULT).text
        else:
            raise TimeoutException("Alert not presented")

    def handle_prompt(self):
        if self.is_alert_presented():
            random_text = self.generate_random_text()
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.send_keys(random_text)
            alert.accept()
            return random_text, alert_text, self.find_element(self.PROMPT_RESULT).text
        else:
            raise TimeoutException("Alert not presented")