from pages.base_page import BasePage
from elements.base_element import BaseElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LinksPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, "linkWrapper")
    HOME_LINK = (By.ID, "simpleLink")
    
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.home_link = BaseElement(self.HOME_LINK, "home Link")

    def click_home_link(self) -> None:
        self.home_link.click()