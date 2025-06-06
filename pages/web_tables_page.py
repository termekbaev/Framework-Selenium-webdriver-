from pages.base_page import BasePage
from selenium.webdriver.common.by import By

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

    def get_users_from_table(self):
        header_row = self.driver.find_elements(*self.HEADER_ROW)
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        users = []
        for row in rows:
            current_user = {}
            cells = row.find_elements(By.CLASS_NAME, "rt-td")
            current_user["first_name"] = next((cells[index].text for index, header in enumerate(header_row) if "first" in header.text.lower()))
            current_user["last_name"] = next((cells[index].text for index, header in enumerate(header_row) if "last" in header.text.lower()))
            current_user["age"] = next((cells[index].text for index, header in enumerate(header_row) if "age" in header.text.lower()))
            current_user["email"] = next((cells[index].text for index, header in enumerate(header_row) if "mail" in header.text.lower()))
            current_user["salary"] = next((cells[index].text for index, header in enumerate(header_row) if "salary" in header.text.lower()))
            current_user["department"] = next((cells[index].text for index, header in enumerate(header_row) if "department" in header.text.lower()))
            users.append(current_user)
        return users
    
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
        raise ValueError(f"User [{user_data}] not in table")