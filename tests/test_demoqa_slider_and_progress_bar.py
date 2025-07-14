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
        assert sliders_page.is_opened(), "Sliders section not opened"

        random_int_value = ValuesGenerator().generate_random_int_value(minimum=0, maximum=100)
        sliders_page.move_slider_to_value(random_int_value)
        assert random_int_value == sliders_page.get_slider_input_value(random_int_value), "Values are different"

        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise