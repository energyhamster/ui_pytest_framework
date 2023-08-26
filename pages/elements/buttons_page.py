import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ButtonsPage(BasePage):
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    CLICK_ME_MESSAGE = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")

    @allure.step("Click on button")
    def click_on_button(self, type_click):
        if type_click == "double_click":
            self.action_double_click(self.element_is_visible(self.DOUBLE_CLICK_BUTTON))
            return self.element_is_present(self.DOUBLE_CLICK_MESSAGE).text
        if type_click == "right_click":
            self.action_right_click(self.element_is_visible(self.RIGHT_CLICK_BUTTON))
            return self.element_is_present(self.RIGHT_CLICK_MESSAGE).text
        if type_click == "click":
            self.element_is_visible(self.CLICK_ME_BUTTON).click()
            return self.element_is_present(self.CLICK_ME_MESSAGE).text
