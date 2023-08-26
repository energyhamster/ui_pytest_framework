import os
import random

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file, generated_subject, generated_state_and_city
from pages.base_page import BasePage


class FormsPage(BasePage):
    # form inputs
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER_RADIOBUTTON = (By.CSS_SELECTOR, f"label[for='gender-radio-{random.randint(1, 3)}']")
    MOBILE_FIELD = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH_FIELD = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    SUBJECT_FIELD = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES_CHECKBOX = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS_FIELD = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    SELECT_STATE = (By.CSS_SELECTOR, "div[id='state']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY = (By.CSS_SELECTOR, "div[id='city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    # form results
    RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")

    @allure.step("Fill form fields")
    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        subject = generated_subject()
        state, city = generated_state_and_city()

        self.element_is_visible(self.FIRST_NAME_FIELD).send_keys(person.first_name)
        self.element_is_visible(self.LAST_NAME_FIELD).send_keys(person.last_name)
        self.element_is_visible(self.EMAIL_FIELD).send_keys(person.email)
        self.element_is_visible(self.GENDER_RADIOBUTTON).click()
        self.element_is_visible(self.MOBILE_FIELD).send_keys(person.mobile)
        self.element_is_visible(self.SUBJECT_FIELD).send_keys(subject)
        self.element_is_visible(self.SUBJECT_FIELD).send_keys(Keys.RETURN)
        self.element_is_visible(self.HOBBIES_CHECKBOX).click()
        self.element_is_present(self.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.CURRENT_ADDRESS_FIELD).send_keys(person.current_address)
        self.element_is_visible(self.SELECT_STATE).click()
        self.element_is_visible(self.STATE_INPUT).send_keys(state)
        self.element_is_visible(self.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.SELECT_CITY).click()
        self.element_is_visible(self.CITY_INPUT).send_keys(city)
        self.element_is_visible(self.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.SUBMIT_BUTTON).click()
        return person

    @allure.step("Form result calculation")
    def form_result(self):
        result_list = self.elements_are_present(self.RESULT_TABLE)
        data = []
        for item in result_list:
            data.append(item.text)
        return data
