from pages.base_page import BasePage
from pages.alerts_page import AlertsPage
from pages.nested_frames_page import NestedFramesPage
from pages.frames_page import FramesPage
from pages.browser_windows_page import BrowserWindowsPage
from selenium.webdriver.common.by import By

class AlertsFrameAndWindowsPage(BasePage):
    ALERTS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-1']")
    NESTED_FRAMES_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3']")
    FRAMES_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-2']")
    BROWSER_WINDOWS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-0']")

    def open_alerts_section(self):
        self.click(self.ALERTS_SECTION)
        return AlertsPage(self.driver)

    def open_nested_frames_section(self):
        self.click(self.NESTED_FRAMES_SECTION)
        return NestedFramesPage(self.driver)

    def open_frames_section(self):
        self.click(self.FRAMES_SECTION)
        return FramesPage(self.driver)
    
    def open_browser_windows_section(self):
        self.click(self.BROWSER_WINDOWS_SECTION)
        return BrowserWindowsPage(self.driver)