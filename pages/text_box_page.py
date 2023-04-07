import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

    def fill_all_fields_and_submit(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.EMAIL).send_keys(email)
        self.element_is_visible(self.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
