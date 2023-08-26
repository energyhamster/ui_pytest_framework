import random

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generator.generator import generated_color
from pages.base_page import BasePage


class AutocompletePage(BasePage):
    MULTIPLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTIPLE_VALUE = (By.CSS_SELECTOR, "div[class='css-12jo7m5 auto-complete__multi-value__label']")
    MULTIPLE_VALUE_REMOVE = (By.CSS_SELECTOR, "div[class='css-xb97g8 auto-complete__multi-value__remove']")
    SINGLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")

    @allure.step("Fill input multiple")
    def fill_input_multiple(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            multiple_input = self.element_is_clickable(self.MULTIPLE_INPUT)
            multiple_input.send_keys(color)
            multiple_input.send_keys(Keys.ENTER)
        return colors

    @allure.step("Remove value from multiple input")
    def remove_value_from_multiple_input(self):
        count_value_before = len(self.elements_are_present(self.MULTIPLE_VALUE))
        remove_button_list = self.elements_are_visible(self.MULTIPLE_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.MULTIPLE_VALUE))
        return count_value_before, count_value_after

    @allure.step("Check color in multiple input")
    def check_color_in_multiple_input(self):
        color_list = self.elements_are_present(self.MULTIPLE_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step("Fill input single")
    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    @allure.step("Check color in single input")
    def check_color_in_single_input(self):
        color = self.element_is_visible(self.SINGLE_VALUE)
        return color.text
