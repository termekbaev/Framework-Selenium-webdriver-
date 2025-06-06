from pages.base_page import BasePage
from pages.links_page import LinksPage
from pages.sample_page import SamplePage
from selenium.webdriver.common.by import By


class BrowserWindowsPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, "browserWindows")
    NEW_TAB_BUTTON = (By.ID, "tabButton")
    ELEMENTS_PANNEL = (By.CLASS_NAME, "element-group")
    ELEMENTS_TAB_FOR_WAITING_COLLAPSE = (By.XPATH, "//*[contains(@class, 'element-list')]")
    LINKS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-5']")

    def click_new_tab_button_that_open_sample_page(self):
        self.click(self.NEW_TAB_BUTTON)
        return SamplePage(self.driver)
    
    def open_links_section(self):
        self.click(self.ELEMENTS_PANNEL)
        self.wait.until(lambda d: "collapsing" not in d.find_element(*self.ELEMENTS_TAB_FOR_WAITING_COLLAPSE).get_attribute("class"))
        self.click(self.LINKS_SECTION)
        return LinksPage(self.driver)