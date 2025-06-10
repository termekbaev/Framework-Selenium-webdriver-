from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from elements.button import Button
from elements.input import Input
from elements.base_element import BaseElement
from typing import Dict, List
import logging

class WebTablesPage(BasePage):
    UNIQUE_ELEMENT = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3' and contains(@class, 'active')]")
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    REGISTRATION_FORM = (By.CLASS_NAME, "modal-content")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    AGE_INPUT = (By.ID, "age")
    EMAIL_INPUT = (By.ID, "userEmail")
    SALARY_INPUT = (By.ID, "salary")
    DEPARTMENT_INPUT = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")
    TABLE_ROWS = (By.XPATH, "//*[@role='rowgroup']/*[not(contains(@class, '-padRow'))]")
    HEADER_ROW = (By.CLASS_NAME, "rt-resizable-header-content")
    DELETE_BUTTON = (By.ID, "delete-record-4")
    
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.add_button = Button(self.ADD_BUTTON, "Add Button")
        self.registration_form = BaseElement(self.REGISTRATION_FORM, "Registration Form")
        self.first_name_input = Input(self.FIRST_NAME_INPUT, "First Name Input")
        self.last_name_input = Input(self.LAST_NAME_INPUT, "Last Name Input")
        self.age_input = Input(self.AGE_INPUT, "Age Input")
        self.email_input = Input(self.EMAIL_INPUT, "Email Input")
        self.salary_input = Input(self.SALARY_INPUT, "Salary Input")
        self.department_input = Input(self.DEPARTMENT_INPUT, "Department Input")
        self.submit_button = Button(self.SUBMIT_BUTTON, "Submit Button")
        self.table_rows = BaseElement(self.TABLE_ROWS, "Table Rows")
        self.header_row = BaseElement(self.HEADER_ROW, "Header Row")
        self.delete_button = Button(self.DELETE_BUTTON, "Delete Button")
        self.logger = logging.getLogger(__name__)

    def click_add_button(self) -> None:
        self.add_button.click()

    def is_registration_form_displayed(self) -> bool:
        return self.registration_form.is_displayed()
    
    def get_all_rows(self) -> List[WebElement]:
        return self.table_rows.find_elements()
    
    def get_table_row_count(self) -> int:
        row_count = len(self.get_all_rows())
        self.logger.info(f"Getting row count = {row_count} in table")
        return row_count
    
    def fill_registration_form(self, user_data: Dict[str, str]) -> None:
        self.logger.info(f"Filling form with data: {user_data}")
        try:
            self.first_name_input.clear_and_type(user_data["first_name"])
            self.last_name_input.clear_and_type(user_data["last_name"])
            self.age_input.clear_and_type(user_data["age"])
            self.email_input.clear_and_type(user_data["email"])
            self.salary_input.clear_and_type(user_data["salary"])
            self.department_input.clear_and_type(user_data["department"])

            self.logger.debug("Form filled successfully")
        except Exception as e:
            self.logger.error(f"Form filling failed: {str(e)}")
            raise

    def click_submit_button(self) -> None:
        self.submit_button.click()
        self.wait.until(lambda d: not d.find_elements(*self.REGISTRATION_FORM))

    def get_users_from_table(self) -> List[Dict[str, str]]:
        header_row = self.header_row.find_elements()
        rows = self.get_all_rows()
        users = []
        self.logger.info(f"Get all users from table:")
        for row in rows:
            current_user = {
                "first_name": "", 
                "last_name": "", 
                "age": "", 
                "email": "", 
                "salary": "", 
                "department": ""
            }
            cells = row.find_elements(By.CLASS_NAME, "rt-td")
            for k in current_user.keys():
                current_user[k] = next((cells[index].text 
                                        for index, header in enumerate(header_row) 
                                        if k.split("_")[0] in header.text.lower()
                                        ))
            users.append(current_user)
            self.logger.info(f"     {current_user}")
        return users
    
    def delete_user(self, user_data) -> None:
        rows = self.table_rows.find_elements()
        for row in rows:
            cells = row.find_elements(By.CLASS_NAME, "rt-td")
            if (cells[0].text == user_data['first_name'] and
                cells[1].text == user_data['last_name'] and
                cells[2].text == user_data['age'] and
                cells[3].text == user_data['email'] and
                cells[4].text == user_data['salary'] and
                cells[5].text == user_data['department']):
                    row.find_element(*self.DELETE_BUTTON).click()
                    self.logger.info(f"User deleted: {user_data} ")
                    return
        raise ValueError(f"User [{user_data}] not in table")