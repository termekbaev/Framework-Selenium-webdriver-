from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.input import Input

class DatePickerPage(BasePage):
    DATE_PICKER_MONTH_YEAR_INPUT = (By.ID, "datePickerMonthYearInput")
    DATE_PICKER_DATE_AND_TIME_INPUT = (By.ID, "dateAndTimePickerInput")

    def __init__(self):
        unique_element = (By.ID, "datePickerContainer")
        super().__init__(unique_element)
        self.date_picker_month_year_input = Input(self.DATE_PICKER_MONTH_YEAR_INPUT, "Date, month and year input")
        self.date_picker_date_and_time_input = Input(self.DATE_PICKER_DATE_AND_TIME_INPUT, "Date and time input")

    def get_date_input_data(self) -> str:
        return self.date_picker_month_year_input.get_attribute("value")
    
    def get_date_and_time_input_data(self) -> str:
        return self.date_picker_date_and_time_input.get_attribute("value")