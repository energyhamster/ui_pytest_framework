import time

from pages.widgets.autocomplete_page import AutocompletePage


class TestAutocomplete:
    page_link = 'https://demoqa.com/auto-complete'

    def test_fill_multiple_autocomplete(self, driver):
        autocomplete_page = AutocompletePage(driver, self.page_link)
        autocomplete_page.open()

        colors = autocomplete_page.fill_input_multiple()
        colors_result = autocomplete_page.check_color_in_multiple_input()

        assert colors == colors_result, "The added colors are missing in the input"

    def test_remove_value_from_multiple_autocomplete(self, driver):
        autocomplete_page = AutocompletePage(driver, self.page_link)
        autocomplete_page.open()

        count_value_before, count_value_after = autocomplete_page.remove_value_from_multiple_input()

        assert count_value_before != count_value_after, "Value was not deleted"

    def test_fill_single_autocomplete(self, driver):
        autocomplete_page = AutocompletePage(driver, self.page_link)
        autocomplete_page.open()

        color = autocomplete_page.fill_input_single()
        color_result = autocomplete_page.check_color_in_single_input()

        assert color == color_result, "The added colors are missing in the input"



