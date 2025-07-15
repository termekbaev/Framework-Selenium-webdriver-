from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.input import Input
from elements.button import Button
from datetime import date

class DatePickerPage(BasePage):
    @staticmethod
    def get_needed_year() -> int:
        needed_year = date.today().year
        while needed_year % 4 != 0:
            needed_year += 1
        return needed_year
    
    DATE_PICKER_MONTH_YEAR_INPUT = (By.ID, "datePickerMonthYearInput")
    DATE_PICKER_DATE_AND_TIME_INPUT = (By.ID, "dateAndTimePickerInput")
    NEEDED_YEAR = (By.XPATH, f"//*[@class='react-datepicker__year-select']/option[@value='{get_needed_year()}']")
    NEEDED_MONTH = (By.XPATH, "//*[@class='react-datepicker__month-select']/option[@value='1']")
    NEEDED_DAY = (By.XPATH, "//*[@class='react-datepicker__day react-datepicker__day--029']")

    def __init__(self):
        unique_element = (By.ID, "datePickerContainer")
        super().__init__(unique_element)
        self.date_picker_month_year_input = Input(self.DATE_PICKER_MONTH_YEAR_INPUT, "Date, month and year input")
        self.date_picker_date_and_time_input = Input(self.DATE_PICKER_DATE_AND_TIME_INPUT, "Date and time input")
        self.needed_year = Button(self.NEEDED_YEAR, "Needed year")
        self.needed_month = Button(self.NEEDED_MONTH, "Needed month(February)")
        self.needed_day = Button(self.NEEDED_DAY, "Needed day(29)")

    def get_date_input_data(self) -> str:
        return self.date_picker_month_year_input.get_attribute("value")
    
    def get_date_and_time_input_data(self) -> str:
        return self.date_picker_date_and_time_input.get_attribute("value")

    def select_next_29_february(self) -> None:
        self.date_picker_month_year_input.click()
        if date.today().year % 4 != 0:
            self.needed_year.click()
        self.needed_month.click()
        self.needed_day.click()