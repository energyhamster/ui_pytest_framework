import random

from pages.web_tables_page import WebTablesPage


class TestWebTables:
    page_link = 'https://demoqa.com/webtables'

    def test_web_table_add_person(self, driver):
        web_tables_page = WebTablesPage(driver, self.page_link)
        web_tables_page.open()

        new_person = web_tables_page.add_new_person()
        table_result = web_tables_page.check_new_added_person()

        assert new_person in table_result, "The new person doesn't added in web table"

    def test_web_table_search_person(self, driver):
        web_tables_page = WebTablesPage(driver, self.page_link)
        web_tables_page.open()

        key_word = web_tables_page.add_new_person()[random.randint(0, 5)]
        web_tables_page.search_person(key_word)
        table_result = web_tables_page.check_search_person()

        assert key_word in table_result, "The person was not found in the table"

    def test_web_table_update_person_info(self, driver):
        web_tables_page = WebTablesPage(driver, self.page_link)
        web_tables_page.open()

        updated_value = web_tables_page.update_random_field_of_person_info()
        web_tables_page.search_person(updated_value)
        table_result = web_tables_page.check_search_person()
        assert updated_value in table_result, "The person card has not been changed"

    def test_web_table_delete_person(self, driver):
        web_tables_page = WebTablesPage(driver, self.page_link)
        web_tables_page.open()

        key_word = web_tables_page.add_new_person()[random.randint(0, 5)]
        web_tables_page.search_person(key_word)
        web_tables_page.delete_person()
        text = web_tables_page.check_deleted()
        assert text == "No rows found", "The person card has not been deleted"

    def test_web_table_change_count_row(self, driver):
        web_tables_page = WebTablesPage(driver, self.page_link)
        web_tables_page.open()

        count = web_tables_page.select_up_to_some_rows()
        assert count == [5, 10, 20, 25, 50,
                         100], "The number of rows in the table has not been " \
                               "changed or has changed incorrectly"
