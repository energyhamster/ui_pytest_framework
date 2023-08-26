import allure

from config import BASE_URL
from pages.elements.dynamic_properties_page import DynamicProperties


@allure.feature("Dynamic Properties")
class TestDynamicProperties:
    page_link = BASE_URL + '/dynamic-properties'

    @allure.title("Check that Button is enabled")
    def test_enable_button(self, driver):
        dynamic_properties_page = DynamicProperties(driver, self.page_link)
        dynamic_properties_page.open()

        enable_button = dynamic_properties_page.check_enable_button()
        assert enable_button is True, "Button did not enable after 5 second"

    @allure.title("Check Dynamic Properties of the page")
    def test_dynamic_properties(self, driver):
        dynamic_properties_page = DynamicProperties(driver, self.page_link)
        dynamic_properties_page.open()

        button_before, button_after = dynamic_properties_page.check_changed_of_button_color()
        assert button_before != button_after, "Colors have not been changed"

    @allure.title("Check that Button is appeared")
    def test_appear_button(self, driver):
        dynamic_properties_page = DynamicProperties(driver, self.page_link)
        dynamic_properties_page.open()

        appear_button = dynamic_properties_page.check_appear_of_button()
        assert appear_button is True, "Button did not appear after 5 second"
