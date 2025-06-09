from pages.base_page import BasePage
from pages.inner_frame_page import InnerFramePage
from elements.base_element import BaseElement
from utils.frame_util import FrameUtil
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class OuterFramePage(BasePage):
    OUTER_FRAME_BODY_TAG_WITH_TEXT = (By.TAG_NAME, "body")
    INNER_FRAME = (By.TAG_NAME, "iframe")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.outer_frame_body_tag_with_text = BaseElement(self.OUTER_FRAME_BODY_TAG_WITH_TEXT, "Outer Frame Text")

    def get_outer_frame_text(self) -> str:
        return self.outer_frame_body_tag_with_text.get_text()
    
    def switch_to_inner_frame_and_get_text(self) -> str:
        frame_util = FrameUtil(self.driver)
        frame_util.switch_to_frame(self.INNER_FRAME)
        inner_page = InnerFramePage(self.driver)
        text = inner_page.get_inner_frame_text()
        return text