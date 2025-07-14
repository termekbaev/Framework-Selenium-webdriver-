from pages.base_page import BasePage
from pages.sliders_page import SlidersPage
from elements.button import Button
from selenium.webdriver.common.by import By

class WidgetsPage(BasePage):
    SLIDERS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3']")

    def __init__(self) -> None:
        unique_element = (By.XPATH, "//*[contains(text(), 'Widgets')]//ancestor::*[@class='group-header']/following-sibling::*[contains(@class, 'show')]")
        super().__init__(unique_element)
        self.sliders_section = Button(self.SLIDERS_SECTION, "Sliders Section")

    def open_sliders_section(self) -> SlidersPage:
        self.sliders_section.click()
        return SlidersPage()