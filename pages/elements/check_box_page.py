import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    CHECKBOX_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_CHECKBOXES = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    CHECKBOX_TITLE_TEXT = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT_LIST = (By.CSS_SELECTOR, "span[class='text-success']")

    def open_full_list(self):
        self.element_is_visible(self.EXPAND_ALL_BUTTON).click()

    def click_random_checkboxes(self):
        checkbox_list = self.elements_are_visible(self.CHECKBOX_LIST)
        count = 4
        while count != 0:
            checkbox = checkbox_list[random.randint(0, len(checkbox_list))]
            if count > 0:
                self.go_to_element(checkbox)
                checkbox.click()
                count -= 1
            else:
                break

    def get_checked_checkbox(self):
        checked_checkboxes_list = self.elements_are_present(self.CHECKED_CHECKBOXES)
        data = []
        for checkbox in checked_checkboxes_list:
            checkbox_title_text = checkbox.find_element("xpath", self.CHECKBOX_TITLE_TEXT).text
            data.append(checkbox_title_text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        output_result_list = self.elements_are_present(self.OUTPUT_RESULT_LIST)
        data = []
        for result_item in output_result_list:
            data.append(result_item.text)
        return str(data).replace(' ', '').lower()
