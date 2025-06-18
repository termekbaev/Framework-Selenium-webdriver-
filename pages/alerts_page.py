from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.button import Button
from elements.label import Label
import logging

class AlertsPage(BasePage):
    ALERT_BUTTON = (By.ID, "alertButton")
    CONFIRM_BUTTON = (By.ID, "confirmButton")
    PROMPT_BUTTON = (By.ID, "promtButton")
    CONFIRM_RESULT = (By.ID, "confirmResult")
    PROMPT_RESULT = (By.ID, "promptResult")

    def __init__(self) -> None:
        unique_element = (By.ID, "javascriptAlertsWrapper")
        super().__init__(unique_element)
        self.alert_button = Button(self.ALERT_BUTTON, "Alert Button")
        self.confirm_button = Button(self.CONFIRM_BUTTON, "Confirm Button")
        self.prompt_button = Button(self.PROMPT_BUTTON, "Prompt Button")
        self.confirm_result = Label(self.CONFIRM_RESULT, "Confirm Result")
        self.prompt_result = Label(self.PROMPT_RESULT, "Prompt Result")
        self.logger = logging.getLogger(__name__)

    def click_alert_button(self) -> None:
        self.alert_button.click()
        self.logger.info(f"Opened alert")

    def click_confirm_button(self) -> None:
        self.confirm_button.click()
        self.logger.info(f"Opened confirm")

    def click_prompt_button(self) -> None:
        self.prompt_button.click()
        self.logger.info(f"Opened prompt")

    def get_confirm_result_text(self) -> str:
        return self.confirm_result.get_text()

    def get_prompt_result_text(self) -> str:
        return self.prompt_result.get_text()