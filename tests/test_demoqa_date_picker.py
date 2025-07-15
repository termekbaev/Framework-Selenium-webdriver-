from pages.main_page import MainPage
import logging

logger = logging.getLogger(__name__)

def test_date_picker() -> None:
    logger.info(f"Starting test Demoqa Date Picker")
    try:
        main_page = MainPage()
        assert main_page.is_opened(), "Main page not opened"
        
        widgets_page = main_page.open_widgets_page()
        assert widgets_page.is_opened(), "Widgets page not opened"

        date_picker_page = widgets_page.open_date_picker_section()
        assert date_picker_page.is_opened(), "Date picker page not opened"

        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise