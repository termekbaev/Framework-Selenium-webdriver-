from pages.main_page import MainPage
import logging

logger = logging.getLogger(__name__)

def test_alerts(driver_manager, config):
    driver = driver_manager.driver
    driver.get(config.app_config.main_url)
    
    main_page = MainPage(driver)
    assert main_page.is_opened(), "Main page not opened"
    
    alerts_frame_and_windows_page = main_page.open_alerts_frame_and_windows_page()
    assert alerts_frame_and_windows_page.is_opened(), "Alerts, Frame and Windows page not opened"
    alerts_page = alerts_frame_and_windows_page.open_alerts_section()
    assert alerts_page.is_opened(), "Alerts section not opened"

    alerts_page.click(alerts_page.ALERT_BUTTON)
    alert_text = alerts_page.get_alert_message_and_accept()
    assert alert_text == "You clicked a button", "Incorrect alert text"
    assert not alerts_page.is_alert_presented(), "Alert not closed"

    alerts_page.click(alerts_page.CONFIRM_BUTTON)
    alert_text, confirm_result_message = alerts_page.get_confirm_message_and_confirm_result_message()
    assert alert_text == "Do you confirm action?", "Incorrect confirm text"
    assert not alerts_page.is_alert_presented(), "Alert not closed"
    assert "Ok" in confirm_result_message, "Confirm result not shown, or not 'OK'"

    alerts_page.click(alerts_page.PROMPT_BUTTON)
    entered_random_text, alert_text, prompt_result_message = alerts_page.get_prompt_message_and_prompt_result_message()
    assert alert_text == "Please enter your name", "Incorrect prompt text"
    assert not alerts_page.is_alert_presented(), "Alert not closed"
    assert prompt_result_message == f"You entered {entered_random_text}", "Prompt result mismatch"