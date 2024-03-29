import allure

from config import BASE_URL
from pages.elements.text_box_page import TextBoxPage


@allure.feature("TextBox")
class TestTextBox:
    page_link = BASE_URL + '/text-box'

    @allure.title("Check TextBox")
    def test_text_box_submit(self, driver):
        text_box_page = TextBoxPage(driver, self.page_link)
        text_box_page.open()

        full_name, email, current_address, permanent_address = \
            text_box_page.fill_all_fields_and_submit()

        output_full_name, output_email, output_current_address, output_permanent_address = \
            text_box_page.check_filled_form()

        assert full_name == output_full_name, "The full name doesn't match"
        assert email == output_email, "The email doesn't match"
        assert current_address == output_current_address, "The current address doesn't match"
        assert permanent_address == output_permanent_address, "The permanent address doesn't match"
