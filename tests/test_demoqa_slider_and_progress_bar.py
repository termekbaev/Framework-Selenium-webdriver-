from pages.main_page import MainPage
from utils.browser.values_generator import ValuesGenerator
import logging

logger = logging.getLogger(__name__)

def test_alerts() -> None:
    logger.info(f"Starting test Demoqa Alerts")
    try:
        main_page = MainPage()
        assert main_page.is_opened(), "Main page not opened"
        
        widgets_page = main_page.open_widgets_page()
        assert widgets_page.is_opened(), "Widgets page not opened"

        sliders_page = widgets_page.open_sliders_section()
        assert sliders_page.is_opened(), "Alerts section not opened"

        random_int_value = ValuesGenerator().generate_random_int_value_between_0_and_100()

        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise