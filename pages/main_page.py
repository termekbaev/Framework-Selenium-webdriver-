from pages.alerts_frame_and_windows_page import AlertsFrameAndWindowsPage
from pages.elements_page import ElementsPage
from pages.base_page import BasePage
from pages.widgets_page import WidgetsPage
from elements.button import Button
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    UNIQUE_ELEMENT = (By.CLASS_NAME, "home-content")
    ALERTS_FRAME_AND_WINDOWS_CARD = (By.XPATH, "//*[@fill-rule='evenodd']/following::h5")
    ELEMENTS_CARD = (By.XPATH, "//*[contains(@class, 'top-card')]")
    WIDGETS_CARD = (By.XPATH, "//*[@fill-rule='evenodd']/following::h5/following::h5")

    def __init__(self) -> None:
        super().__init__(self.UNIQUE_ELEMENT)
        self.alerts_frame_card = Button(self.ALERTS_FRAME_AND_WINDOWS_CARD, "Alerts, Frame & Windows Card")
        self.elements_card = Button(self.ELEMENTS_CARD, "Elements Card")
        self.widgets_card = Button(self.WIDGETS_CARD, "Widgets Card")

    def open_alerts_frame_and_windows_page(self) -> AlertsFrameAndWindowsPage:
        self.alerts_frame_card.click()
        return AlertsFrameAndWindowsPage()
    
    def open_elements_page(self) -> ElementsPage:
        self.elements_card.click()
        return ElementsPage()
    
    def open_widgets_page(self) -> WidgetsPage:
        self.widgets_card.click()
        return WidgetsPage()