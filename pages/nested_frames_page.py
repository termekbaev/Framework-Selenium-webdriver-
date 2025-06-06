from pages.base_page import BasePage
from pages.outer_frame_page import OuterFramePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3' and contains(@class, 'active')]")
    OUTER_FRAME = (By.ID, "frame1")

    def get_text_in_frames(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.OUTER_FRAME))
        outer_frame = OuterFramePage(self.driver)
        outer_frame_text, inner_frame_text = outer_frame.get_outer_frame_text(), outer_frame.switch_to_inner_frame_and_get_text()
        self.driver.switch_to.default_content()
        return outer_frame_text, inner_frame_text