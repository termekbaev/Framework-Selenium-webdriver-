from pages.base_page import BasePage
from pages.inner_frame_page import InnerFramePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class OuterFramePage(BasePage):
    OUTER_FRAME_BODY_TAG_WITH_TEXT = (By.TAG_NAME, "body")
    INNER_FRAME = (By.TAG_NAME, "iframe")

    def get_outer_frame_text(self):
        return self.get_element_text(self.OUTER_FRAME_BODY_TAG_WITH_TEXT)
    
    def switch_to_inner_frame_and_get_text(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.INNER_FRAME))
        inner_page = InnerFramePage(self.driver)
        return inner_page.get_inner_frame_text()