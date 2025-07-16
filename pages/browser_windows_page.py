from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.links_page import LinksPage
from pages.frames.sample_page import SamplePage
from elements.button import Button

class BrowserWindowsPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, "browserWindows")
    NEW_TAB_BUTTON = (By.ID, "tabButton")
    ELEMENTS_PANNEL = (By.CLASS_NAME, "element-group")
    ELEMENTS_TAB_FOR_WAITING_COLLAPSE = (By.XPATH, "//*[contains(@class, 'element-list')]")
    LINKS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-5']")

    def __init__(self) -> None:
        super().__init__(self.UNIQUE_ELEMENT)
        self.new_tab_button = Button(self.NEW_TAB_BUTTON, "New Tab Button")
        self.elements_pannel = Button(self.ELEMENTS_PANNEL, "Elements Pannel")
        self.links_section = Button(self.LINKS_SECTION, "Links Section")

    def click_new_tab_button_that_open_sample_page(self) -> SamplePage:
        self.new_tab_button.click()
        return SamplePage()
    
    def open_links_section(self) -> LinksPage:
        self.elements_pannel.click()
        self.wait.until(lambda d: "collapsing" not in d.find_element(*self.ELEMENTS_TAB_FOR_WAITING_COLLAPSE).get_attribute("class"))
        self.links_section.click()
        return LinksPage()