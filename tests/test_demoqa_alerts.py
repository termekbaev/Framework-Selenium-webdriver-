from utils.browser.alerts_util import AlertUtil
from utils.config.data_reader import DataReader
from pages.main_page import MainPage
import logging

logger = logging.getLogger(__name__)

def test_alerts(alerts_test_data: DataReader) -> None:
    logger.info(f"Starting test Demoqa Alerts")
    try:
        test_data = alerts_test_data.get_alert_texts()
        main_page = MainPage()
        assert main_page.is_opened(), "Main page not opened"
        
        alerts_frame_and_windows_page = main_page.open_alerts_frame_and_windows_page()
        assert alerts_frame_and_windows_page.is_opened(), "Alerts, Frame and Windows page not opened"

        alerts_page = alerts_frame_and_windows_page.open_alerts_section()
        assert alerts_page.is_opened(), "Alerts section not opened"

        alerts_util = AlertUtil()

        alerts_page.click_alert_button()
        assert alerts_util.is_alert_present(), "Alert not opened"

        alert_text = alerts_util.get_alert_text()
        alerts_util.accept_alert()
        assert alert_text == test_data["alert_text"], "Incorrect alert text"
        assert not alerts_util.is_alert_present(), "Alert not closed"

        alerts_page.click_confirm_button()
        assert alerts_util.is_alert_present(), "Confirm not opened"

        confirm_text = alerts_util.get_alert_text()
        alerts_util.accept_alert()
        confirm_result = alerts_page.get_confirm_result_text()
        assert confirm_text == test_data["confirm_text"], "Incorrect confirm text"
        assert test_data["confirm_result"] in confirm_result, "Confirm result not shown, or not 'OK'"

        alerts_page.click_prompt_button()
        assert alerts_util.is_alert_present(), "Prompt not opened"

        prompt_text = alerts_util.get_alert_text()
        random_text = alerts_util.generate_random_text()
        alerts_util.send_text_to_alert(random_text)
        alerts_util.accept_alert()
        prompt_result = alerts_page.get_prompt_result_text()
        assert prompt_text == test_data["prompt_text"], "Incorrect prompt text"
        assert prompt_result == f"{test_data["prompt_result_prefix"]}{random_text}", "Prompt result mismatch"
        
        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise