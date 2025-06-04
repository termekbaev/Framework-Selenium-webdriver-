from pages.base_page import BasePage
from pages.web_tables_page import WebTablesPage
from selenium.webdriver.common.by import By

class ElementsPage(BasePage):
    WEB_TABLES_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3']")

    def open_web_tables_section(self):
        self.click(self.WEB_TABLES_SECTION)
        return WebTablesPage(self.driver)