from pages.main_page import MainPage
from utils.browser.values_generator import ValuesGenerator
from datetime import date
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

        value_generator = ValuesGenerator()
        assert value_generator.generate_current_datetime_string_in_format("%m/%d/%Y") == \
            date_picker_page.get_date_input_data(),\
            "Dates not matched"
        assert value_generator.generate_current_datetime_string_in_format("%B %d, %Y %I:%M %p").replace(" 0", " ") == \
            date_picker_page.get_date_and_time_input_data(), \
            "Dates not matched"

        date_picker_page.select_next_29_february()
        assert value_generator.generate_datetime_string_in_format(
                    year=date_picker_page.get_needed_year(), 
                    month=2, 
                    day=29, 
                    format_string="%m/%d/%Y") == \
            date_picker_page.get_date_input_data(), \
            "Dates not matched"

        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise