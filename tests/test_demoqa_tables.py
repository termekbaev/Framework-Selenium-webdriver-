from pages.main_page import MainPage
import logging
import pytest
import json

logger = logging.getLogger(__name__)

with open("config/test_web_tables_data.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("user_data", test_data["users"], ids=lambda x: f"{x['first_name']} {x['last_name']}")
def test_web_tables(driver_manager, config, user_data):
    driver = driver_manager.driver
    driver.get(config.app_config.main_url)
    
    main_page = MainPage(driver)
    assert main_page.is_opened(), "Main page not opened"
    logger.info(f"Testing user: {user_data['first_name']}, {user_data['last_name']}")
    
    elements_page = main_page.open_elements_page()
    assert elements_page.is_opened(), "Elements page not opened"
    web_tables_page = elements_page.open_web_tables_section()
    assert web_tables_page.is_opened(), "Web Tables section not opened"
    
    initial_row_count = web_tables_page.get_table_row_count()
    
    web_tables_page.click_add_button()
    assert web_tables_page.is_registration_form_displayed(), "Registration form not displayed"
    
    web_tables_page.fill_registration_form(user_data)
    web_tables_page.click_submit_button()
    
    assert not web_tables_page.is_registration_form_displayed(), "Registration form still on display"
    assert web_tables_page.get_table_row_count() == initial_row_count + 1, "New row not added"
    
    assert web_tables_page.is_user_in_table(user_data), "There is no user data in table"
    logger.info("It's OK! User data in table")
    
    web_tables_page.delete_user(user_data)
    assert web_tables_page.get_table_row_count() == initial_row_count, "Initial row count != row count after delete"
    assert not web_tables_page.is_user_in_table(user_data), "User still in table"
    logger.info(f"User {user_data['first_name']} deleted from table")
