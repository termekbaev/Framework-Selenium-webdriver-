from pages.main_page import MainPage
import logging
import os

logger = logging.getLogger(__name__)

def test_date_picker() -> None:
    logger.info(f"Starting test Demoqa Date Picker")
    try:
        main_page = MainPage()
        assert main_page.is_opened(), "Main page not opened"
        
        elements_page = main_page.open_elements_page()
        assert elements_page.is_opened(), "Elements page not opened"

        upload_and_download_page = elements_page.open_upload_and_download_section()
        assert upload_and_download_page.is_opened(), "Upload and download section not opened"

        download_path = upload_and_download_page.click_on_download_button_and_get_download_path(r"C:\Users\t-erm\Downloads")
        assert os.path.exists(download_path), "File not downloaded"

        upload_and_download_page.upload_file(download_path)
        file_name = download_path.split("\\")[-1]
        assert upload_and_download_page.get_uploaded_file_name() == file_name, \
            "File not uploaded"

        upload_and_download_page.delete_file(download_path)
        assert not os.path.exists(download_path), "File not deleted"

        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise