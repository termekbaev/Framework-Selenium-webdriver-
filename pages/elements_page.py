from pages.base_page import BasePage
from pages.web_tables_page import WebTablesPage
from elements.button import Button
from selenium.webdriver.common.by import By

class ElementsPage(BasePage):
    WEB_TABLES_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3']")

    def __init__(self) -> None:
        unique_element = (By.XPATH, "//*[contains(text(), 'Elements')]//ancestor::*[@class='group-header']/following-sibling::*[contains(@class, 'show')]")
        super().__init__(unique_element)
        self.web_tables_section = Button(self.WEB_TABLES_SECTION, "Web Tables Section")

    def open_web_tables_section(self) -> WebTablesPage:
        self.web_tables_section.click()
        return WebTablesPage()