from pages.base_page import BasePage
from pages.sample_page import SamplePage
from utils.frame_util import FrameUtil
from selenium.webdriver.common.by import By
from typing import Tuple

class FramesPage(BasePage):
    FRAME_TOP = (By.ID, "frame1")
    FRAME_BOTTOM = (By.ID, "frame2")

    def __init__(self):
        unique_element = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-2' and contains(@class, 'active')]")
        super().__init__(unique_element)

    def __get_frame_text(self, frame_locator: Tuple[By, str]) -> str:
        frame_util = FrameUtil()
        frame_util.switch_to_frame(frame_locator)
        frame_page = SamplePage()
        frame_text = frame_page.get_sample_page_text()
        frame_util.switch_to_default_content()
        return frame_text
    
    def switch_and_get_top_frame_text(self) -> str:
        return self.__get_frame_text(self.FRAME_TOP)
    
    def switch_and_get_bottom_frame_text(self) -> str:
        return self.__get_frame_text(self.FRAME_BOTTOM)