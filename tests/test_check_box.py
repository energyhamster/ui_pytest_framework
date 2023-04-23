from pages.check_box_page import CheckBoxPage


class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()

        check_box_page.open_full_list()
        check_box_page.click_random_checkboxes()
        input_checkboxes = check_box_page.get_checked_checkbox()
        output_results = check_box_page.get_output_result()
        assert input_checkboxes == output_results, "Checkboxes have not been selected"
