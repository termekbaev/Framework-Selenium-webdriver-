from utils.alerts_util import AlertUtil
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AlertsPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, "javascriptAlertsWrapper")
    ALERT_BUTTON = (By.ID, "alertButton")
    CONFIRM_BUTTON = (By.ID, "confirmButton")
    PROMPT_BUTTON = (By.ID, "promtButton")
    CONFIRM_RESULT = (By.ID, "confirmResult")
    PROMPT_RESULT = (By.ID, "promptResult")

    def __init__(self, driver):
        super().__init__(driver)
        self.alert_util = AlertUtil(driver)

    def click_alert_button(self):
        self.click(self.ALERT_BUTTON)

    def click_confirm_button(self):
        self.click(self.CONFIRM_BUTTON)

    def click_prompt_button(self):
        self.click(self.PROMPT_BUTTON)

    def get_confirm_result_text(self):
        return self.get_element_text(self.CONFIRM_RESULT)

    def get_prompt_result_text(self):
        return self.get_element_text(self.PROMPT_RESULT)