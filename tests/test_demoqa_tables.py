from pages.main_page import MainPage
import logging

logger = logging.getLogger(__name__)

def test_web_tables(driver_manager, config):
    driver = driver_manager.driver
    driver.get(config.app_config.main_url)
    
    main_page = MainPage(driver)
    assert main_page.is_opened_main_page(), "Main page not opened"
    logger.info("Main page opened")
    
    elements_page = main_page.open_elements_page()
    web_tables_page = elements_page.open_web_tables_section()
    assert web_tables_page.is_opened_web_tables_section(), "Web Tables section not opened"
    logger.info("Web Tables section opened")
    
    initial_row_count = web_tables_page.get_table_row_count()
    
    web_tables_page.click_add_button()
    assert web_tables_page.is_registration_form_displayed(), "Registration form not displayed"
    logger.info("Registration form displayed")
    
    web_tables_page.fill_registration_form()
    web_tables_page.click_submit_button()
    
    assert not web_tables_page.is_registration_form_displayed(), "Registration form still on display"
    assert web_tables_page.get_table_row_count() == initial_row_count + 1, "New row not added"
    logger.info(f"User {web_tables_page.user_data['first_name']} added in table")
    
    assert web_tables_page.is_user_in_table(), "There is no user data in table"
    logger.info("It's OK! User data in table")
    
    web_tables_page.delete_user()
    assert web_tables_page.get_table_row_count() == initial_row_count, "Initial row count != row count after delete"
    assert not web_tables_page.is_user_in_table(), "User still in table"
    logger.info(f"User {web_tables_page.user_data['first_name']} deleted from table")
