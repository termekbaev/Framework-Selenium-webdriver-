import pytest
from pages.main_page import MainPage
from pages.alerts_page import AlertsPage
import logging

logger = logging.getLogger(__name__)

def test_alerts(driver_manager, config):
    driver = driver_manager.driver
    driver.get(config.app_config.main_url)
    
    main_page = MainPage(driver)
    assert main_page.is_opened_main_page(), "Main page not opened"
    logger.info("Main page opened")
    
    main_page.open_alerts_page()
    alerts_page = AlertsPage(driver)
    alerts_page.open_alerts_section()
    assert alerts_page.is_opened_alerts_section(), "Alerts section not opened"
    logger.info("Alerts section is on the screen")

    alerts_page.click(alerts_page.ALERT_BUTTON)
    alert_text = alerts_page.check_alert_message_then_accept()
    assert alert_text == "You clicked a button", "Incorrect alert text"
    logger.info(f"Alert handled with text: {alert_text}")

    assert not alerts_page.is_alert_presented(), "Alert not closed"
    logger.info(f"Alert closed")



    alerts_page.click(alerts_page.CONFIRM_BUTTON)
    alert_text, confirm_result_message = alerts_page.handle_confirm()
    assert alert_text == "Do you confirm action?", "Incorrect confirm text"
    logger.info(f"Alert handled with text: {alert_text}")

    assert not alerts_page.is_alert_presented(), "Alert not closed"
    logger.info(f"Alert closed")

    assert "Ok" in confirm_result_message, "Confirm result not shown, or not 'OK'"
    logger.info(f"Text {confirm_result_message} is displayed near the button")



    alerts_page.click(alerts_page.PROMPT_BUTTON)
    entered_random_text, alert_text, prompt_result_message = alerts_page.handle_prompt()
    assert alert_text == "Please enter your name", "Incorrect prompt text"
    logger.info(f"Alert handled with text: {alert_text}")

    assert not alerts_page.is_alert_presented(), "Alert not closed"
    logger.info(f"Alert closed")

    assert prompt_result_message == f"You entered {entered_random_text}", "Prompt result mismatch"
    logger.info(f"Prompt handled with text: {entered_random_text}")