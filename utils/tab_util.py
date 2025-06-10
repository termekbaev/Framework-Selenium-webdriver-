from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List
import logging

class TabUtil:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def get_current_window_handle(self) -> str:
        return self.driver.current_window_handle

    def get_all_window_handles(self) -> List[str]:
        return self.driver.window_handles

    def switch_to_tab(self, window_handle: str) -> None:
        try:
            self.driver.switch_to.window(window_handle)
            self.logger.info(f"Switching to tab: Title: '{self.driver.title}' | Handle: {window_handle}")
        except NoSuchWindowException:
            self.logger.error(f"Tab not found: {window_handle}")
            raise

    def switch_to_new_tab(self, close_old_tab: bool = False) -> str:
        old_tab = self.driver.current_window_handle
        new_tab = self.driver.window_handles[-1]
        self.switch_to_tab(new_tab)
        
        if close_old_tab:
            self.switch_to_tab(old_tab)
            self.logger.info(f"Tab closed. Title: '{self.driver.title}' | Handle: {self.driver.current_window_handle}")
            self.driver.close()
            self.switch_to_tab(new_tab)
        return new_tab

    def close_current_tab(self) -> None:
        self.logger.info(f"Tab closed. Title: '{self.driver.title}' | Handle: {self.driver.current_window_handle}")
        self.driver.close()

    def is_tab_open(self, window_handle: str) -> bool:
        try:
            return window_handle in self.driver.window_handles
        except NoSuchWindowException:
            return False