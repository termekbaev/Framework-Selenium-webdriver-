from pages.main_page import MainPage
from typing import Dict
import logging
import pytest
import json

logger = logging.getLogger(__name__)

with open("test_data/web_tables.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("user_data", test_data["users"], ids=lambda x: f"{x['first_name']} {x['last_name']}")
def test_web_tables(user_data: Dict[str, str]) -> None:
    logger.info(f"Starting test for user: {user_data['first_name']} {user_data['last_name']}")
    try:
        main_page = MainPage()
        assert main_page.is_opened(), "Main page not opened"
        
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
        
        users_from_table = web_tables_page.get_users_from_table()
        assert user_data in users_from_table, "There is no user data in tables"

        web_tables_page.delete_user(user_data)
        assert web_tables_page.get_table_row_count() == initial_row_count, "Initial row count != row count after delete"
        users = web_tables_page.get_users_from_table()
        assert user_data not in users, "User still in table" 

        logger.info("Test completed successfully")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        raise