import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_date
from pages.base_page import BasePage


class DatePickerPage(BasePage):
    # Select Date
    DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    # Select Date and Time
    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_TIME_SELECT_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_TIME_SELECT_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_AND_TIME_SELECT_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item']")
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")

    @allure.step("Select date")
    def select_date(self):
        date = next(generated_date())
        input_date = self.elements_are_visible(self.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step("Select date and time")
    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.elements_are_visible(self.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.DATE_AND_TIME_SELECT_MONTH).click()
        self.set_date_item_from_list(self.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.DATE_AND_TIME_SELECT_YEAR).click()
        self.set_date_item_from_list(self.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.DATE_AND_TIME_SELECT_TIME_LIST, date.time)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step("Set date by text")
    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    @allure.step("Set date item from list")
    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break
