import random

import allure
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage


class WebTablesPage(BasePage):
    # add person form
    USER_FORM = (By.CSS_SELECTOR, "form[id='userForm']")
    USER_FORM_INPUT_LIST = (By.CSS_SELECTOR, "input[required]")
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")
    USER_FORM_FIELDS_LIST = (By.CSS_SELECTOR, "div[class='col-md-3 col-sm-12']")
    USER_FORM_FIELDS_SIBLING = ".//following-sibling::div/input"

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")
    NO_ROWS_FOUND_TEXT = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_DROPDOWN = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

    # person info
    person_info = next(generated_person())
    person_info_dict = {
        0: person_info.first_name,
        1: person_info.last_name,
        2: person_info.email,
        3: person_info.age,
        4: person_info.salary,
        5: person_info.department,
    }

    @allure.step("Add new person in the table")
    def add_new_person(self, count=1):
        while count != 0:
            self.element_is_visible(self.ADD_BUTTON).click()
            self.element_is_visible(self.FIRST_NAME_INPUT).send_keys(self.person_info.first_name)
            self.element_is_visible(self.LAST_NAME_INPUT).send_keys(self.person_info.last_name)
            self.element_is_visible(self.EMAIL_INPUT).send_keys(self.person_info.email)
            self.element_is_visible(self.AGE_INPUT).send_keys(self.person_info.age)
            self.element_is_visible(self.SALARY_INPUT).send_keys(self.person_info.salary)
            self.element_is_visible(self.DEPARTMENT_INPUT).send_keys(self.person_info.department)
            self.element_is_visible(self.SUBMIT_BUTTON).click()
            self.element_is_not_visible(self.SUBMIT_BUTTON)

            count -= 1
            return [self.person_info.first_name, self.person_info.last_name, str(self.person_info.age),
                    self.person_info.email, str(self.person_info.salary), self.person_info.department]

    @allure.step("Check new added person")
    def check_new_added_person(self):
        people_list = self.elements_are_present(self.FULL_PEOPLE_LIST)

        data = []

        for item in people_list:
            data.append(item.text.splitlines())

        return data

    @allure.step("Search person")
    def search_person(self, key_word):
        self.element_is_visible(self.SEARCH_INPUT).send_keys(key_word)

    @allure.step("Check search person")
    def check_search_person(self):
        delete_button = self.element_is_present(self.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.ROW_PARENT)
        return row.text.splitlines()

    @allure.step("Update random field of person info")
    def update_random_field_of_person_info(self):
        self.element_is_present(self.EDIT_BUTTON).click()
        inputs_list = self.elements_are_present(self.USER_FORM_INPUT_LIST)

        index = random.randint(0, len(inputs_list) - 1)

        count = 0

        for field in inputs_list:
            if count == index:
                field.clear()
                field.send_keys(self.person_info_dict[index])
                self.element_is_present(self.SUBMIT_BUTTON).click()
                self.element_is_not_visible(self.SUBMIT_BUTTON)
            count += 1

        return self.person_info_dict[index]

    @allure.step("Delete person")
    def delete_person(self):
        self.element_is_visible(self.DELETE_BUTTON).click()

    @allure.step("Check delete")
    def check_deleted(self):
        return self.element_is_present(self.NO_ROWS_FOUND_TEXT).text

    @allure.step("Select up to some row")
    def select_up_to_some_rows(self):
        count_rows = [5, 10, 20, 25, 50, 100]
        data = []

        for count in count_rows:
            count_row_button = self.go_to_element(self.element_is_visible(self.COUNT_ROW_DROPDOWN))
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{count}']")).click()
            data.append(self.check_count_rows())
        return data

    @allure.step("Check count row")
    def check_count_rows(self):
        list_rows = self.elements_are_present(self.FULL_PEOPLE_LIST)
        return len(list_rows)
