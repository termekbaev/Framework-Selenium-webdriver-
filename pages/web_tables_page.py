from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class WebTablesPage(BasePage):
    WEB_TABLES_SECTION_CHECK = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3' and contains(@class, 'active')]")
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
    DELETE_BUTTON = (By.ID, "delete-record-4")

    def is_opened_web_tables_section(self):
        return self.is_element_displayed(self.WEB_TABLES_SECTION_CHECK)
    
    def click_add_button(self):
        self.click(self.ADD_BUTTON)

    def is_registration_form_displayed(self):
        return self.is_element_displayed(self.REGISTRATION_FORM)
    
    def get_table_row_count(self):
        return len(self.driver.find_elements(*self.TABLE_ROWS))
    
    def fill_registration_form(self, user_data):
        self.find_element(self.FIRST_NAME_INPUT).send_keys(user_data['first_name'])
        self.find_element(self.LAST_NAME_INPUT).send_keys(user_data['last_name'])
        self.find_element(self.AGE_INPUT).send_keys(user_data['age'])
        self.find_element(self.EMAIL_INPUT).send_keys(user_data['email'])
        self.find_element(self.SALARY_INPUT).send_keys(user_data['salary'])
        self.find_element(self.DEPARTMENT_INPUT).send_keys(user_data['department'])

    def click_submit_button(self):
        self.click(self.SUBMIT_BUTTON)
        self.wait.until(lambda d: not d.find_elements(*self.REGISTRATION_FORM))

    def is_user_in_table(self, user_data):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        for row in rows:
            cells = row.find_elements(By.CLASS_NAME, "rt-td")
            if (cells[0].text == user_data['first_name'] and
                cells[1].text == user_data['last_name'] and
                cells[2].text == user_data['age'] and
                cells[3].text == user_data['email'] and
                cells[4].text == user_data['salary'] and
                cells[5].text == user_data['department']):
                return True
        return False
    
    def delete_user(self, user_data):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        for row in rows:
            cells = row.find_elements(By.CLASS_NAME, "rt-td")
            if (cells[0].text == user_data['first_name'] and
                cells[1].text == user_data['last_name'] and
                cells[2].text == user_data['age'] and
                cells[3].text == user_data['email'] and
                cells[4].text == user_data['salary'] and
                cells[5].text == user_data['department']):
                    row.find_element(*self.DELETE_BUTTON).click()
                    return
        raise ValueError(f"User with first name {user_data['first_name']} not in table")