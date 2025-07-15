from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class UploadAndDownloadPage(BasePage):
    def __init__(self):
        unique_element = (By.ID, "downloadButton")
        super().__init__(unique_element)