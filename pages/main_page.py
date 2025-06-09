from pages.alerts_frame_and_windows_page import AlertsFrameAndWindowsPage
from pages.elements_page import ElementsPage
from pages.base_page import BasePage
from elements.button import Button
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class MainPage(BasePage):
    UNIQUE_ELEMENT = (By.CLASS_NAME, "home-content")
    ALERTS_FRAME_AND_WINDOWS_CARD = (By.XPATH, "//*[@fill-rule='evenodd']/following::h5")
    ELEMENTS_CARD = (By.XPATH, "//*[contains(@class, 'top-card')]")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.alerts_frame_card = Button(self.ALERTS_FRAME_AND_WINDOWS_CARD, "Alerts, Frame & Windows Card")
        self.elements_card = Button(self.ELEMENTS_CARD, "Elements Card")

    def open_alerts_frame_and_windows_page(self) -> AlertsFrameAndWindowsPage:
        self.alerts_frame_card.click()
        return AlertsFrameAndWindowsPage(self.driver)
    
    def open_elements_page(self) -> ElementsPage:
        self.elements_card.click()
        return ElementsPage(self.driver)