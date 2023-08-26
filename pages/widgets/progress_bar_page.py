import random
import time

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProgressBarPage(BasePage):
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")

    @allure.step("Change progress bar value")
    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(self.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 5))
        progress_bar_button.click()
        value_after = self.element_is_present(self.PROGRESS_BAR_VALUE).text
        return value_before, value_after
