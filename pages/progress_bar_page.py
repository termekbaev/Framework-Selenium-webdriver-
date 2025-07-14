from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProgressBarPage(BasePage):
    def __init__(self) -> None:
        unique_element = (By.ID, "progressBarContainer")
        super().__init__(unique_element)
    
    