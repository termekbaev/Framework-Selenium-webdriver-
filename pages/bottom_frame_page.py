from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from elements.base_element import BaseElement

class BottomFramePage(BasePage):
    BOTTOM_FRAME_TEXT = (By.ID, "sampleHeading")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.bottom_frame_text = BaseElement(self.BOTTOM_FRAME_TEXT, "Bottom Frame Text")

    def get_bottom_frame_text(self) -> str:
        return self.bottom_frame_text.get_text()