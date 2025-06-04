from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LinksPage(BasePage):
    LINKS_SECTION_CHECK = (By.ID, "linkWrapper")
    HOME_LINK = (By.ID, "simpleLink")
    
    def is_opened_links_page(self):
        return self.is_element_displayed(self.LINKS_SECTION_CHECK)
    
    def click_home_link(self):
        self.click(self.HOME_LINK)