from pages.alerts_frame_and_windows_page import AlertsFrameAndWindowsPage
from pages.elements_page import ElementsPage
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    UNIQUE_ELEMENT = (By.CLASS_NAME, "home-content")
    ALERTS_FRAME_AND_WINDOWS_CARD = (By.XPATH, "//*[@fill-rule='evenodd']/following::h5")
    ELEMENTS_CARD = (By.XPATH, "//*[contains(@class, 'top-card')]")

    def is_opened_main_page(self):
        return self.is_element_displayed(self.UNIQUE_ELEMENT)

    def open_alerts_frame_and_windows_page(self):
        self.click(self.ALERTS_FRAME_AND_WINDOWS_CARD)
        return AlertsFrameAndWindowsPage(self.driver)
    
    def open_elements_page(self):
        self.click(self.ELEMENTS_CARD)
        return ElementsPage(self.driver)