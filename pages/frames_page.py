from pages.base_page import BasePage
from pages.top_frame_page import TopFramePage
from pages.bottom_frame_page import BottomFramePage
from utils.frame_util import FrameUtil
from selenium.webdriver.common.by import By

class FramesPage(BasePage):
    UNIQUE_ELEMENT = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-2' and contains(@class, 'active')]")
    FRAME_TOP = (By.ID, "frame1")
    FRAME_BOTTOM = (By.ID, "frame2")

    def switch_and_get_top_frame_text(self):
        frame_util = FrameUtil(self.driver)
        frame_util.switch_to_frame(self.FRAME_TOP)
        top_frame_page = TopFramePage(self.driver)
        top_frame_text = top_frame_page.get_top_frame_text()
        frame_util.switch_to_default_content()
        return top_frame_text
    
    def switch_and_get_bottom_frame_text(self):
        frame_util = FrameUtil(self.driver)
        frame_util.switch_to_frame(self.FRAME_BOTTOM)
        bottom_frame_page = BottomFramePage(self.driver)
        bottom_frame_text = bottom_frame_page.get_bottom_frame_text()
        frame_util.switch_to_default_content()
        return bottom_frame_text