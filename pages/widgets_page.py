from pages.base_page import BasePage
from pages.slider_page import SliderPage
from pages.date_picker_page import DatePickerPage
from elements.button import Button
from selenium.webdriver.common.by import By

class WidgetsPage(BasePage):
    UNIQUE_ELEMENT = (By.XPATH, "//*[contains(text(), 'Widgets')]//ancestor::*[@class='group-header']/following-sibling::*[contains(@class, 'show')]")
    SLIDERS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3']")
    DATE_PICKER_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-2']")

    def __init__(self) -> None:
        super().__init__(self.UNIQUE_ELEMENT)
        self.slider_section = Button(self.SLIDERS_SECTION, "Sliders section")
        self.date_picker_section = Button(self.DATE_PICKER_SECTION, "Date picker section")

    def open_slider_section(self) -> SliderPage:
        self.slider_section.click()
        return SliderPage()
    
    def open_date_picker_section(self) -> DatePickerPage:
        self.date_picker_section.click()
        return DatePickerPage()