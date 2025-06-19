from pages.main_page import MainPage
from utils.config.data_reader import DataReader
import logging

logger = logging.getLogger(__name__)

def test_frames(frames_test_data: DataReader) -> None:
    logger.info(f"Starting test Demoqa Frames")
    try:    
        test_data = frames_test_data.get_frames_texts()
        main_page = MainPage()
        assert main_page.is_opened(), "Main page not opened"

        alerts_frame_and_windows_page = main_page.open_alerts_frame_and_windows_page()
        assert alerts_frame_and_windows_page.is_opened(), "Alerts, Frame and Windows page not opened"
        nested_frames_page = alerts_frame_and_windows_page.open_nested_frames_section()   
        assert nested_frames_page.is_opened(), "Nested frames page not opened"

        outer_frame_text, inner_frame_text = nested_frames_page.get_text_in_frames()
        assert test_data["parent_frame"] == outer_frame_text and \
               test_data["child_frame"] == inner_frame_text, "Some of frame texts not found"

        frames_page = alerts_frame_and_windows_page.open_frames_section()
        assert frames_page.is_opened(), "Frames page not opened"

        top_frame_text = frames_page.switch_and_get_top_frame_text()
        bottom_frame_text = frames_page.switch_and_get_bottom_frame_text()
        assert top_frame_text == bottom_frame_text, "Frame1 text != Frame2 text"

        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise