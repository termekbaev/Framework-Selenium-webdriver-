from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SamplePage(BasePage):
    UNIQUE_ELEMENT = (By.ID, "sampleHeading")