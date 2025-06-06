from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InnerFramePage(BasePage):
    INNER_FRAME_P_TAG_WITH_TEXT = (By.TAG_NAME, "p")

    def get_inner_frame_text(self):
        return self.find_element(self.INNER_FRAME_P_TAG_WITH_TEXT).text