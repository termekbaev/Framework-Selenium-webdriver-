from pages.base_page import BasePage
from elements.label import Label
from selenium.webdriver.common.by import By

class SamplePage(BasePage):
    def __init__(self) -> None:
        unique_element = (By.ID, "sampleHeading")
        super().__init__(unique_element)
        self.unique_text = Label(unique_element, "Unique Text")

    def get_sample_page_text(self) -> str:
        return self.unique_text.get_text()