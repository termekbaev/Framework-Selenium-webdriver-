from selenium.common.exceptions import NoSuchWindowException

class TabUtil:
    def __init__(self, driver):
        self.driver = driver

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_all_window_handles(self):
        return self.driver.window_handles

    def switch_to_tab(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def switch_to_new_tab(self, close_old_tab=False):
        old_tab = self.driver.current_window_handle
        new_tab = self.driver.window_handles[-1]
        self.switch_to_tab(new_tab)
        
        if close_old_tab:
            self.switch_to_tab(old_tab)
            self.driver.close()
            self.switch_to_tab(new_tab)
        return new_tab

    def close_current_tab(self):
        self.driver.close()

    def is_tab_open(self, window_handle):
        try:
            return window_handle in self.driver.window_handles
        except NoSuchWindowException:
            return False