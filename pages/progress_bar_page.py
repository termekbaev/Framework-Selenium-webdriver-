from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.button import Button
from elements.base_element import BaseElement
import logging

class ProgressBarPage(BasePage):
    START_AND_STOP_BUTTON = (By.ID, "startStopButton")
    PROGRESS_BAR = (By.XPATH, "//*[@role='progressbar']")

    def __init__(self) -> None:
        unique_element = (By.ID, "progressBarContainer")
        super().__init__(unique_element)
        self.start_and_stop_button = Button(self.START_AND_STOP_BUTTON, "Start/stop button")
        self.progress_bar = BaseElement(self.PROGRESS_BAR, "Progress bar")
        self.logger = logging.getLogger(__name__)

    def click_start_button_then_stop_on_value_or_near(self, secret_value: int) -> None:
        self.start_and_stop_button.click()
        self.wait.until(lambda _ : int(self.progress_bar.get_attribute("aria-valuenow")) >= secret_value)
        self.start_and_stop_button.click()
        progress_bar_value = int(self.progress_bar.get_attribute("aria-valuenow"))
        self.logger.info(f"Try to stop progress bar on value '{secret_value}', and progress bar stoped on '{progress_bar_value}'")

    def get_progress_bar_value(self) -> int:
        return int(self.progress_bar.get_attribute("aria-valuenow"))
    