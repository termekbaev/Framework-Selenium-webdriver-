from pages.main_page import MainPage
import logging

logger = logging.getLogger(__name__)

def test_browser_windows_and_links(driver_manager, config):
    driver = driver_manager.driver
    driver.get(config.app_config.main_url)
    main_page = MainPage(driver)
    assert main_page.is_opened(), "Main page is not opened"
    
    alerts_frame_and_windows_page = main_page.open_alerts_frame_and_windows_page()
    browser_windows_page = alerts_frame_and_windows_page.open_browser_windows_section()
    assert browser_windows_page.is_opened(), "Browser Windows page is not opened"
    
    initial_window = driver.current_window_handle
    browser_windows_page.click_new_tab_button()
    new_window = [window for window in driver.window_handles if window != initial_window][0]
    driver.switch_to.window(new_window)
    assert sample_page.is_opened(), "New tab doesn't contain 'sample' in URL"
    
    driver.close()
    driver.switch_to.window(initial_window)
    assert browser_windows_page.is_opened(), "Didn't return to Browser Windows page"
    
    links_page = browser_windows_page.open_links_section()
    assert links_page.is_opened(), "Links page is not opened"
    
    links_page.click_home_link()
    all_windows = driver.window_handles
    assert len(all_windows) == 2, "Expected exactly 2 tabs after clicking Home link"
    driver.switch_to.window(all_windows[-1])
    assert main_page.is_opened(), "Main page is not opened in new tab"
    
    driver.switch_to.window(all_windows[0])
    assert links_page.is_opened(), "Didn't return to Links page"