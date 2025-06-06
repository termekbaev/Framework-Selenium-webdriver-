from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LinksPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, "linkWrapper")
    HOME_LINK = (By.ID, "simpleLink")
    
    def click_home_link(self):
        self.click(self.HOME_LINK)