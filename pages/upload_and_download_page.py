from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.button import Button
from elements.input import Input
from elements.label import Label
import os
import logging
import time

class UploadAndDownloadPage(BasePage):
    FILE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    UPLOADED_FILE_PATH = (By.ID, "uploadedFilePath")

    def __init__(self) -> None:
        unique_element = (By.ID, "downloadButton")
        super().__init__(unique_element)
        self.logger = logging.getLogger(__name__)
        self.download_button = Button(unique_element, "Download button")
        self.file_input = Input(self.FILE_INPUT, "File input")
        self.uploaded_file_path = Label(self.UPLOADED_FILE_PATH, "Uploaded file path")

    def click_on_download_button_and_get_download_path(self, download_dir: str) -> str:
        self.download_button.click()
        filename = "sampleFile.jpeg"
        file_path = os.path.join(download_dir, filename)
        time.sleep(0.5)
        self.wait.until(lambda _ : os.path.exists(file_path))
        return file_path
    
    def delete_file(self, path: str) -> None:
        if os.path.exists(path):
            os.remove(path)
            self.logger.info(f"Файл {path} успешно удалён")
        else:
            self.logger.info(f"Файл {path} не существует")

    def upload_file(self, path: str) -> None:
        self.file_input.type(path)

    def get_uploaded_file_name(self) -> str:
        return self.uploaded_file_path.get_text().split("\\")[-1]