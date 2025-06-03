from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FramesPage(BasePage):
    FRAMES_PAGE_CHECK = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-2' and contains(@class, 'active')]")
    FRAME_TOP = (By.ID, "frame1")
    FRAME_BOTTOM = (By.ID, "frame2")
    FRAME_TEXT = (By.TAG_NAME, "h1")

    def is_opened_frames_page(self):
        return self.is_element_displayed(self.FRAMES_PAGE_CHECK)

    def get_top_frame_text(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.FRAME_TOP))
        text = self.get_element_text(self.FRAME_TEXT)
        self.driver.switch_to.default_content()
        return text
    
    def get_bottom_frame_text(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.FRAME_BOTTOM))
        text = self.get_element_text(self.FRAME_TEXT)
        self.driver.switch_to.default_content()
        return text