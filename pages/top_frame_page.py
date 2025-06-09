from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from elements.base_element import BaseElement

class TopFramePage(BasePage):
    TOP_FRAME_TEXT = (By.ID, "sampleHeading")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.top_frame_text = BaseElement(self.TOP_FRAME_TEXT, "Top Frame Text")

    def get_top_frame_text(self) -> str:
        return self.top_frame_text.get_text()