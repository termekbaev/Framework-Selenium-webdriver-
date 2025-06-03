from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class NestedFramesPage(BasePage):
    NESTED_FRAMES_PAGE_CHECK = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3' and contains(@class, 'active')]")
    PARENT_FRAME = (By.ID, "frame1")
    CHILD_FRAME = (By.XPATH, "//body/iframe")
    PARENT_TEXT = (By.TAG_NAME, "body")
    CHILD_TEXT = (By.TAG_NAME, "p")

    def is_opened_nested_frames_page(self):
        return self.is_element_displayed(self.NESTED_FRAMES_PAGE_CHECK)

    def switch_to_parent_frame_and_return_text(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.PARENT_FRAME))
        return self.get_element_text(self.PARENT_TEXT)
    
    def switch_to_child_frame_and_return_text(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.CHILD_FRAME))
        return self.get_element_text(self.CHILD_TEXT)
    
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()