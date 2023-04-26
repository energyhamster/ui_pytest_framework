from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage


class WebTablesPage(BasePage):
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")

    def add_new_person(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            self.element_is_visible(self.ADD_BUTTON).click()
            self.element_is_visible(self.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.SUBMIT_BUTTON).click()

            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.FULL_PEOPLE_LIST)

        data = []

        for item in people_list:
            data.append(item.text.splitlines())

        return data
