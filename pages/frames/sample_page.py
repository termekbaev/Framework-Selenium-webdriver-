from pages.base_page import BasePage
from elements.label import Label
from selenium.webdriver.common.by import By

class SamplePage(BasePage):
    UNIQUE_ELEMENT = (By.ID, "sampleHeading")

    def __init__(self) -> None:
        super().__init__(self.UNIQUE_ELEMENT)
        self.unique_text = Label(self.UNIQUE_ELEMENT, "Unique Text")

    def get_sample_page_text(self) -> str:
        return self.unique_text.get_text()