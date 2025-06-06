from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class BottomFramePage(BasePage):
    BOTTOM_FRAME_TEXT = (By.ID, "sampleHeading")

    def get_bottom_frame_text(self):
        return self.find_element(self.BOTTOM_FRAME_TEXT).text