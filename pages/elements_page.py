from pages.base_page import BasePage
from pages.web_tables_page import WebTablesPage
from elements.button import Button
from selenium.webdriver.common.by import By

class ElementsPage(BasePage):
    UNIQUE_ELEMENT = (By.XPATH, "//*[@viewBox='0 0 448 512']//ancestor::*[@class='group-header']/following-sibling::*[contains(@class, 'show')]")
    WEB_TABLES_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-3']")

    def __init__(self) -> None:
        super().__init__()
        self.web_tables_section = Button(self.WEB_TABLES_SECTION, "Web Tables Section")

    def open_web_tables_section(self) -> WebTablesPage:
        self.web_tables_section.click()
        return WebTablesPage()