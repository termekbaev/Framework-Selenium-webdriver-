from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.label import Label

class TopFramePage(BasePage):
    TOP_FRAME_TEXT = (By.ID, "sampleHeading")

    def __init__(self) -> None:
        super().__init__()
        self.top_frame_text = Label(self.TOP_FRAME_TEXT, "Top Frame Text")

    def get_top_frame_text(self) -> str:
        return self.top_frame_text.get_text()