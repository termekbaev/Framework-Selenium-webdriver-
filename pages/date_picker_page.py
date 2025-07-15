from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DatePickerPage(BasePage):
    def __init__(self):
        unique_element = (By.ID, "datePickerContainer")
        super().__init__(unique_element)