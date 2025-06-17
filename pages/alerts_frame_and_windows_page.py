from pages.base_page import BasePage
from pages.alerts_page import AlertsPage
from pages.nested_frames_page import NestedFramesPage
from pages.frames_page import FramesPage
from pages.browser_windows_page import BrowserWindowsPage
from elements.button import Button
from selenium.webdriver.common.by import By

class AlertsFrameAndWindowsPage(BasePage):
    UNIQUE_ELEMENT = (By.XPATH, "//*[@fill-rule='evenodd']//ancestor::*[@class='group-header']/following-sibling::*[contains(@class, 'show')]")
    ALERTS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-1']")
    NESTED_FRAMES_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3']")
    FRAMES_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-2']")
    BROWSER_WINDOWS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-0']")

    def __init__(self) -> None:
        super().__init__()
        self.alerts_section = Button(self.ALERTS_SECTION, "Alerts Section")
        self.nested_frames_section = Button(self.NESTED_FRAMES_SECTION, "Nested Frames Section")
        self.frames_section = Button(self.FRAMES_SECTION, "Frames Section")
        self.browser_windows_section = Button(self.BROWSER_WINDOWS_SECTION, "Browser Windows Section")

    def open_alerts_section(self) -> AlertsPage:
        self.alerts_section.click()
        return AlertsPage()

    def open_nested_frames_section(self) -> NestedFramesPage:
        self.nested_frames_section.click()
        return NestedFramesPage()

    def open_frames_section(self) -> FramesPage:
        self.frames_section.click()
        return FramesPage()
    
    def open_browser_windows_section(self) -> BrowserWindowsPage:
        self.browser_windows_section.click()
        return BrowserWindowsPage()