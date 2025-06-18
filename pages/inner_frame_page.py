from pages.base_page import BasePage
from elements.label import Label
from selenium.webdriver.common.by import By

class InnerFramePage(BasePage):
    INNER_FRAME_P_TAG_WITH_TEXT = (By.TAG_NAME, "p")

    def __init__(self) -> None:
        super().__init__(unique_element_locator=None, check_is_opened=False)
        self.inner_frame_p_tag_with_text = Label(self.INNER_FRAME_P_TAG_WITH_TEXT, "Inner Frame Text")

    def get_inner_frame_text(self) -> str:
        return self.inner_frame_p_tag_with_text.get_text()