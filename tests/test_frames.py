from pages.main_page import MainPage
from pages.alerts_frame_and_windows_page import AlertsFrameAndWindowsPage
from pages.frames_page import FramesPage
from pages.nested_frames_page import NestedFramesPage
import logging

logger = logging.getLogger(__name__)

def test_alerts(driver_manager, config):
    driver = driver_manager.driver
    driver.get(config.app_config.main_url)
    
    main_page = MainPage(driver)
    assert main_page.is_opened_main_page(), "Main page not opened"
    logger.info("Main page opened")

    main_page.open_alerts_frame_and_windows_page()
    alerts_frame_and_windows_page = AlertsFrameAndWindowsPage(driver)
    alerts_frame_and_windows_page.open_nested_frames_section()
    nested_frames_page = NestedFramesPage(driver)    
    assert nested_frames_page.is_opened_nested_frames_page(), "Nested frames page not opened"
    logger.info("Nested Frames page opened")

    parent_text = nested_frames_page.switch_to_parent_frame_and_return_text()
    assert "Parent frame" in parent_text, "'Parent frame' text not found"

    child_text = nested_frames_page.switch_to_child_frame_and_return_text()
    assert "Child Iframe" in child_text, "'Child Iframe' text not found"
    logger.info("Texts 'Parent frame' and 'Child Iframe' are on the page ")
    nested_frames_page.switch_to_default_content()

    frames_page = FramesPage(driver)
    alerts_frame_and_windows_page.open_frames_section()
    assert frames_page.is_opened_frames_page(), "Frames page not opened"
    logger.info("Frames page opened")

    top_frame_text = frames_page.get_top_frame_text()
    bottom_frame_text = frames_page.get_bottom_frame_text()
    assert top_frame_text == bottom_frame_text, "Frame1 text != Frame2 text"
    logger.info("Top frame text == bottom frame text")