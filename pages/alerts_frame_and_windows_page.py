from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AlertsFrameAndWindowsPage(BasePage):
    ALERTS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-1']")
    NESTED_FRAMES_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3']")
    FRAMES_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-2']")

    def open_alerts_section(self):
        self.click(self.ALERTS_SECTION)

    def open_nested_frames_section(self):
        self.click(self.NESTED_FRAMES_SECTION)

    def open_frames_section(self):
        self.click(self.FRAMES_SECTION)