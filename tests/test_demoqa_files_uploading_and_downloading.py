from pages.main_page import MainPage
from utils.config.data_reader import DataReader
import logging

logger = logging.getLogger(__name__)

def test_date_picker(date_picker_test_data: DataReader) -> None:
    logger.info(f"Starting test Demoqa Date Picker")
    try:
        test_data = date_picker_test_data.get_date_picker_data()
        main_page = MainPage()
        assert main_page.is_opened(), "Main page not opened"
        
        elements_page = main_page.open_elements_page()
        assert elements_page.is_opened(), "Elements page not opened"

        upload_and_download_page = elements_page.open_upload_and_download_section()
        assert upload_and_download_page.is_opened(), "Upload and download section not opened"

        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise