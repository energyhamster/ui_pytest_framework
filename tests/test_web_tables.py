from pages.web_tables_page import WebTablesPage


class TestWebTables:
    def test_web_table_add_person(self, driver):
        web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
        web_tables_page.open()

        new_person = web_tables_page.add_new_person()
        table_result = web_tables_page.check_new_added_person()

        assert new_person in table_result, "The new person doesn't added in web table"
