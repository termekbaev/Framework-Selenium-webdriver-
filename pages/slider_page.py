from utils.browser.driver_manager import DriverManager
from pages.base_page import BasePage
from pages.progress_bar_page import ProgressBarPage
from elements.button import Button
from elements.input import Input
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging

class SliderPage(BasePage):
    SLIDER = (By.XPATH, "//*[@id='sliderContainer']/descendant::input[@type='range']")
    SLIDER_INPUT_VALUE = (By.XPATH, "//*[@id='sliderValue']")
    PROGRESS_BAR_SECTION = (By.XPATH, "//*[contains(@class, 'active')]/following::li")

    def __init__(self) -> None:
        unique_element = (By.XPATH, "//*[@id='sliderContainer']")
        super().__init__(unique_element)
        self.slider = Input(self.SLIDER, "Slider")
        self.slider_input_value = Input(self.SLIDER_INPUT_VALUE, "Slider input value")
        self.progress_bar_section = Button(self.PROGRESS_BAR_SECTION, "Progress bar section")
        self.logger = logging.getLogger(__name__)
        
    def move_slider_to_value(self, value: int) -> None:
        slider_width = self.slider.find_element().size["width"]
        action = ActionChains(DriverManager().driver)
        for offset in range(int((value / 100) * slider_width - slider_width / 2 - slider_width // 100), slider_width + 1, slider_width // 100):
            action.click_and_hold(self.slider.find_element()).move_by_offset(offset, 0).release().perform()
            if int(self.slider.get_attribute("value")) == value:
                self.logger.info(f"Moved slider to value {value}")
                break

    def get_slider_input_value(self, value_for_waiting_check: int) -> int:
        self.wait.until(lambda _: value_for_waiting_check == int(self.slider.get_attribute("value")),
                            "Bad slider working"
                        )
        input_value = int(self.slider_input_value.get_attribute("value"))
        self.logger.info(f"Get input value '{input_value}' for check")
        return input_value
    
    def open_progress_bar_section(self) -> ProgressBarPage:
        self.progress_bar_section.click()
        return ProgressBarPage()
        