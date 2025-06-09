from pages.base_page import BasePage
from elements.base_element import BaseElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class InnerFramePage(BasePage):
    INNER_FRAME_P_TAG_WITH_TEXT = (By.TAG_NAME, "p")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.inner_frame_p_tag_with_text = BaseElement(self.INNER_FRAME_P_TAG_WITH_TEXT, "Inner Frame Text")

    def get_inner_frame_text(self) -> str:
        return self.inner_frame_p_tag_with_text.get_text()