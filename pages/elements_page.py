from pages.base_page import BasePage
from pages.web_tables_page import WebTablesPage
from pages.upload_and_download_page import UploadAndDownloadPage
from elements.button import Button
from selenium.webdriver.common.by import By

class ElementsPage(BasePage):
    UNIQUE_ELEMENT = (By.XPATH, "//*[contains(text(), 'Elements')]//ancestor::*[@class='group-header']/following-sibling::*[contains(@class, 'show')]")
    WEB_TABLES_SECTION = (By.ID, "item-3")
    UPLOAD_AND_DOWNLOAD_SECTION = (By.ID, "item-7")

    def __init__(self) -> None:
        super().__init__(self.UNIQUE_ELEMENT)
        self.web_tables_section = Button(self.WEB_TABLES_SECTION, "Web Tables Section")
        self.upload_and_download_section = Button(self.UPLOAD_AND_DOWNLOAD_SECTION, "Upload and download files section")

    def open_web_tables_section(self) -> WebTablesPage:
        self.web_tables_section.click()
        return WebTablesPage()
    
    def open_upload_and_download_section(self) -> UploadAndDownloadPage:
        self.upload_and_download_section.click()
        return UploadAndDownloadPage()