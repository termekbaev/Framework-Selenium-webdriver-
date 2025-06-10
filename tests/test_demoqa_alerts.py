from utils.alerts_util import AlertUtil
from utils.driver_manager import DriverManager
from utils.config_reader import ConfigReader
from pages.main_page import MainPage
import logging
import random
import string

logger = logging.getLogger(__name__)

def generate_random_text(length: int = 20) -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def test_alerts(driver_manager: DriverManager, config: ConfigReader) -> None:
    logger.info(f"Starting test Demoqa Alerts")
    try:
        driver = driver_manager.driver
        driver.get(config.app_config.main_url)
        
        main_page = MainPage(driver)
        assert main_page.is_opened(), "Main page not opened"
        
        alerts_frame_and_windows_page = main_page.open_alerts_frame_and_windows_page()
        assert alerts_frame_and_windows_page.is_opened(), "Alerts, Frame and Windows page not opened"

        alerts_page = alerts_frame_and_windows_page.open_alerts_section()
        assert alerts_page.is_opened(), "Alerts section not opened"

        alerts_util = AlertUtil(driver)

        alerts_page.click_alert_button()
        assert alerts_util.is_alert_present(), "Alert not opened"

        alert_text = alerts_util.get_alert_text()
        alerts_util.accept_alert()
        assert alert_text == "You clicked a button", "Incorrect alert text"
        assert not alerts_util.is_alert_present(), "Alert not closed"

        alerts_page.click_confirm_button()
        assert alerts_util.is_alert_present(), "Confirm not opened"

        confirm_text = alerts_util.get_alert_text()
        alerts_util.accept_alert()
        confirm_result = alerts_page.get_confirm_result_text()
        assert confirm_text == "Do you confirm action?", "Incorrect confirm text"
        assert "Ok" in confirm_result, "Confirm result not shown, or not 'OK'"

        alerts_page.click_prompt_button()
        assert alerts_util.is_alert_present(), "Prompt not opened"

        prompt_text = alerts_util.get_alert_text()
        random_text = generate_random_text()
        alerts_util.send_text_to_alert(random_text)
        alerts_util.accept_alert()
        prompt_result = alerts_page.get_prompt_result_text()
        assert prompt_text == "Please enter your name", "Incorrect prompt text"
        assert prompt_result == f"You entered {random_text}", "Prompt result mismatch"
        
        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise