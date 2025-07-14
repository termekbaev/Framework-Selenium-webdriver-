from utils.browser.driver_manager import DriverManager
from pages.base_page import BasePage
from elements.button import Button
from elements.input import Input
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class SlidersPage(BasePage):
    SLIDER = (By.XPATH, "//*[@id='sliderContainer']/descendant::input[@type='range']")
    SLIDER_INPUT_VALUE = (By.XPATH, "//*[@id='sliderValue']")

    def __init__(self) -> None:
        unique_element = (By.XPATH, "//*[@id='sliderContainer']")
        super().__init__(unique_element)
        self.slider = Input(self.SLIDER, "Slider")
        self.slider_input_value = Input(self.SLIDER_INPUT_VALUE, "Slider input value")
        
    def move_slider_to_value(self, value: int) -> None:
        slider_width = self.slider.find_element().size["width"]
        action = ActionChains(DriverManager().driver)
        for offset in range(int((value / 100) * slider_width - slider_width / 2 - slider_width // 100), slider_width + 1, slider_width // 100):
            action.click_and_hold(self.slider.find_element()).move_by_offset(offset, 0).release().perform()
            print(offset, self.slider.get_attribute("value"))
            if int(self.slider.get_attribute("value")) == value:
                break

    def get_slider_input_value(self, value_for_waiting_check: int) -> int:
        self.wait.until(lambda _: value_for_waiting_check == int(self.slider.get_attribute("value")),
                            "Bad slider working"
                        )
        return int(self.slider_input_value.get_attribute("value"))
        