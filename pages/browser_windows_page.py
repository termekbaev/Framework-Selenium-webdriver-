from pages.base_page import BasePage
from pages.links_page import LinksPage
from selenium.webdriver.common.by import By


class BrowserWindowsPage(BasePage):
    BROWSER_WINDOWS_SECTION_CHECK = (By.ID, "browserWindows")
    NEW_TAB_BUTTON = (By.ID, "tabButton")
    SAMPLE_PAGE_ELEMENT = (By.ID, "sampleHeading")
    ELEMENTS_PANNEL = (By.CLASS_NAME, "element-group")
    ELEMENTS_TAB_FOR_WAITING_COLLAPSE = (By.XPATH, "//*[contains(@class, 'element-list')]")
    LINKS_SECTION = (By.XPATH, "//*[contains(@class, 'show')]//*[@id='item-5']")

    def click_new_tab_button(self):
        self.click(self.NEW_TAB_BUTTON)

    def is_opened_browser_windows_page(self):
        return self.is_element_displayed(self.BROWSER_WINDOWS_SECTION_CHECK)
    
    def is_sample_page_opened(self):
        return self.is_element_displayed(self.SAMPLE_PAGE_ELEMENT)
    
    def open_links_section(self):
        self.click(self.ELEMENTS_PANNEL)
        self.wait.until(lambda d: "collapsing" not in d.find_element(*self.ELEMENTS_TAB_FOR_WAITING_COLLAPSE).get_attribute("class"))
        self.click(self.LINKS_SECTION)
        return LinksPage(self.driver)