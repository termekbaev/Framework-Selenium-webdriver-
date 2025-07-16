from pages.main_page import MainPage
from utils.config.data_reader import DataReader
from utils.browser.values_generator import ValuesGenerator
import logging

logger = logging.getLogger(__name__)

def test_slider_and_progress_bar(progress_bar_test_data: DataReader) -> None:
    logger.info(f"Starting test Demoqa Alerts")
    try:
        test_data = progress_bar_test_data.get_progress_bar_data()
        main_page = MainPage()
        assert main_page.is_opened(), "Main page not opened"
        
        widgets_page = main_page.open_widgets_page()
        assert widgets_page.is_opened(), "Widgets page not opened"

        slider_page = widgets_page.open_slider_section()
        assert slider_page.is_opened(), "Sliders section not opened"

        random_int_value = ValuesGenerator().generate_random_int_value(minimum=0, maximum=100)
        slider_page.move_slider_to_value(random_int_value)
        assert random_int_value == slider_page.get_slider_input_value(random_int_value), "Values are different"

        progress_bar_page = slider_page.open_progress_bar_section()
        assert progress_bar_page.is_opened(), "Progress bar section not opened"

        progress_bar_page.click_start_button_then_stop_on_value_or_near(test_data["secret_value"], test_data["error"])
        assert test_data["secret_value"] - test_data["error"] <= \
                progress_bar_page.get_progress_bar_value() <= \
                test_data["secret_value"] + test_data["error"], \
                f"Bad value, not between {test_data['secret_value'] - test_data["error"]} \
                        and {test_data['secret_value'] + test_data['error']}"

        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise