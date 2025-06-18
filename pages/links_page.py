from pages.base_page import BasePage
from elements.button import Button
from selenium.webdriver.common.by import By

class LinksPage(BasePage):
    HOME_LINK = (By.ID, "simpleLink")
    
    def __init__(self) -> None:
        unique_element = (By.ID, "linkWrapper")
        super().__init__(unique_element)
        self.home_link = Button(self.HOME_LINK, "Home Link")

    def click_home_link(self) -> None:
        self.home_link.click()