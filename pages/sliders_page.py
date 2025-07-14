from pages.base_page import BasePage
from elements.button import Button
from selenium.webdriver.common.by import By

class SlidersPage(BasePage):


    def __init__(self) -> None:
        unique_element = (By.XPATH, "//*[@id='sliderContainer']")
        super().__init__(unique_element)
        