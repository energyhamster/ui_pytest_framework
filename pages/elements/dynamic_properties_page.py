import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DynamicProperties(BasePage):
    ENABLE_BUTTON = (By.CSS_SELECTOR, "button[id='enableAfter']")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id='colorChange']")
    VISIBLE_AFTER_5_SECOND_BUTTON = (By.CSS_SELECTOR, "button[id='visibleAfter']")

    def check_enable_button(self):
        try:
            self.element_is_clickable(self.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    def check_changed_of_button_color(self):
        color_button = self.element_is_present(self.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(6)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.VISIBLE_AFTER_5_SECOND_BUTTON)
        except TimeoutException:
            return False
        return True
