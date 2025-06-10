from pages.main_page import MainPage
from utils.tab_util import TabUtil
from utils.driver_manager import DriverManager
from utils.config_reader import ConfigReader
import logging

logger = logging.getLogger(__name__)

def test_handles(driver_manager: DriverManager, config: ConfigReader) -> None:
    logger.info(f"Starting test Demoqa Handles")
    try:
        driver = driver_manager.driver
        driver.get(config.app_config.main_url)
        tab_util = TabUtil(driver)
        main_page = MainPage(driver)
        assert main_page.is_opened(), "Main page is not opened"
        
        alerts_frame_and_windows_page = main_page.open_alerts_frame_and_windows_page()
<<<<<<< HEAD
        assert alerts_frame_and_windows_page.is_opened(), "Alerts, Frame & Windows page is not opened"
=======
>>>>>>> 19f1b34191763c2dd788802b6ec3defc06e01290
        browser_windows_page = alerts_frame_and_windows_page.open_browser_windows_section()
        assert browser_windows_page.is_opened(), "Browser Windows page is not opened"
        
        initial_window = tab_util.get_current_window_handle()
        sample_page = browser_windows_page.click_new_tab_button_that_open_sample_page()
        new_window = tab_util.switch_to_new_tab()
        assert sample_page.is_opened(), "New tab doesn't contain 'sample' in URL"
        
        tab_util.close_current_tab()
        tab_util.switch_to_tab(initial_window)
        assert browser_windows_page.is_opened(), "Didn't return to Browser Windows page"
        
        links_page = browser_windows_page.open_links_section()
        assert links_page.is_opened(), "Links page is not opened"
        
        links_page.click_home_link()
        all_windows = tab_util.get_all_window_handles()
        assert len(all_windows) == 2, "Expected exactly 2 tabs after clicking 'Home' link"
        tab_util.switch_to_new_tab()
        assert main_page.is_opened(), "Main page is not opened in new tab"
        
        tab_util.switch_to_tab(all_windows[0])
        assert links_page.is_opened(), "Didn't return to Links page"

        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise