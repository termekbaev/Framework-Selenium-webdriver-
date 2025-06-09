from pages.base_page import BasePage
from pages.inner_frame_page import InnerFramePage
from utils.frame_util import FrameUtil
from selenium.webdriver.common.by import By

class OuterFramePage(BasePage):
    OUTER_FRAME_BODY_TAG_WITH_TEXT = (By.TAG_NAME, "body")
    INNER_FRAME = (By.TAG_NAME, "iframe")

    def get_outer_frame_text(self):
        return self.get_element_text(self.OUTER_FRAME_BODY_TAG_WITH_TEXT)
    
    def switch_to_inner_frame_and_get_text(self):
        frame_util = FrameUtil(self.driver)
        frame_util.switch_to_frame(self.INNER_FRAME)
        inner_page = InnerFramePage(self.driver)
        text = inner_page.get_inner_frame_text()
        return text