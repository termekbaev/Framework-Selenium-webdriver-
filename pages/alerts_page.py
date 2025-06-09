from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from elements.button import Button
from elements.base_element import BaseElement

class AlertsPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, "javascriptAlertsWrapper")
    ALERT_BUTTON = (By.ID, "alertButton")
    CONFIRM_BUTTON = (By.ID, "confirmButton")
    PROMPT_BUTTON = (By.ID, "promtButton")
    CONFIRM_RESULT = (By.ID, "confirmResult")
    PROMPT_RESULT = (By.ID, "promptResult")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.alert_button = Button(self.ALERT_BUTTON, "Alert Button")
        self.confirm_button = Button(self.CONFIRM_BUTTON, "Confirm Button")
        self.prompt_button = Button(self.PROMPT_BUTTON, "Prompt Button")
        self.confirm_result = BaseElement(self.CONFIRM_RESULT, "Confirm Result")
        self.prompt_result = BaseElement(self.PROMPT_RESULT, "Prompt Result")

    def click_alert_button(self) -> None:
        self.alert_button.click()

    def click_confirm_button(self) -> None:
        self.confirm_button.click()

    def click_prompt_button(self) -> None:
        self.prompt_button.click()

    def get_confirm_result_text(self) -> str:
        return self.confirm_result.get_text()

    def get_prompt_result_text(self) -> str:
        return self.prompt_result.get_text()