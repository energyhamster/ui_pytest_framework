import allure

from config import BASE_URL
from pages.widgets.date_picker_page import DatePickerPage


class TestDatePicker:
    page_link = BASE_URL + '/date-picker'

    @allure.title("Check that date was changed")
    def test_change_date(self, driver):
        date_picker_page = DatePickerPage(driver, self.page_link)
        date_picker_page.open()

        value_date_before, value_date_after = date_picker_page.select_date()

        assert value_date_before != value_date_after, "The date has not been changed"

    @allure.title("Check that date and time was changed")
    def test_change_date_and_time(self, driver):
        date_picker_page = DatePickerPage(driver, self.page_link)
        date_picker_page.open()

        value_date_before, value_date_after = date_picker_page.select_date_and_time()

        assert value_date_before != value_date_after, "The date has not been changed"
