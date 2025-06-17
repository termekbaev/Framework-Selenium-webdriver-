from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.label import Label

class BottomFramePage(BasePage):
    BOTTOM_FRAME_TEXT = (By.ID, "sampleHeading")

    def __init__(self) -> None:
        super().__init__()
        self.bottom_frame_text = Label(self.BOTTOM_FRAME_TEXT, "Bottom Frame Text")

    def get_bottom_frame_text(self) -> str:
        return self.bottom_frame_text.get_text()