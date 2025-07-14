from pages.base_page import BasePage
from pages.slider_page import SliderPage
from elements.button import Button
from selenium.webdriver.common.by import By

class WidgetsPage(BasePage):
    SLIDERS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3']")

    def __init__(self) -> None:
        unique_element = (By.XPATH, "//*[contains(text(), 'Widgets')]//ancestor::*[@class='group-header']/following-sibling::*[contains(@class, 'show')]")
        super().__init__(unique_element)
        self.slider_section = Button(self.SLIDERS_SECTION, "Sliders Section")

    def open_slider_section(self) -> SliderPage:
        self.slider_section.click()
        return SliderPage()