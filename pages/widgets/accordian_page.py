import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccordianPage(BasePage):
    FIRST_ACCORDIAN_TITLE = (By.CSS_SELECTOR, "div[id='section1Heading']")
    FIRST_ACCORDIAN_BODY = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    SECOND_ACCORDIAN_TITLE = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECOND_ACCORDIAN_BODY = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    THIRD_ACCORDIAN_TITLE = (By.CSS_SELECTOR, "div[id='section3Heading']")
    THIRD_ACCORDIAN_BODY = (By.CSS_SELECTOR, "div[id='section3Content'] p")

    @allure.step("Check accordian")
    def check_accordian(self, accordian_num):
        accordian = {
            'first_section':
                {
                    'title': self.FIRST_ACCORDIAN_TITLE,
                    'body': self.FIRST_ACCORDIAN_BODY
                },
            'second_section':
                {
                    'title': self.SECOND_ACCORDIAN_TITLE,
                    'body': self.SECOND_ACCORDIAN_BODY
                },
            'third_section':
                {
                    'title': self.THIRD_ACCORDIAN_TITLE,
                    'body': self.THIRD_ACCORDIAN_BODY
                }
        }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_body = self.element_is_visible(accordian[accordian_num]['body']).text
        except TimeoutException:
            section_title.click()
            section_body = self.element_is_visible(accordian[accordian_num]['body']).text

        return [section_title.text, len(section_body)]
