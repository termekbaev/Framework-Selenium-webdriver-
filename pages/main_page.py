from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    UNIQUE_ELEMENT = (By.CLASS_NAME, "home-content")
    ALERTS_FRAME_AND_WINDOWS_CARD = (By.XPATH, "//*[@fill-rule='evenodd']/following::h5")

    def is_opened_main_page(self):
        return self.is_element_displayed(self.UNIQUE_ELEMENT)

    def open_alerts_page(self):
        self.find_element(self.ALERTS_FRAME_AND_WINDOWS_CARD).click()