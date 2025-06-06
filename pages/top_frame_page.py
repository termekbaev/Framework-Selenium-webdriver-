from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TopFramePage(BasePage):
    TOP_FRAME_TEXT = (By.ID, "sampleHeading")

    def get_top_frame_text(self):
        return self.find_element(self.TOP_FRAME_TEXT).text