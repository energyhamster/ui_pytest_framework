import random
import time

from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AlertsPage(BasePage):
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_APPEAR_AFTER_5_SECONDS_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_RESULT_TEXT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_RESULT_TEXT = (By.CSS_SELECTOR, "span[id='promptResult']")

    def check_see_alert(self):
        self.element_is_visible(self.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.ALERT_APPEAR_AFTER_5_SECONDS_BUTTON).click()
        time.sleep(6)

        try:
            alert_window = self.driver.switch_to.alert
            return alert_window
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.CONFIRM_RESULT_TEXT).text
        return text_result

    def check_prompt_alert(self):
        text = f"autotest {random.randint(0, 9999999)}"
        self.element_is_visible(self.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.PROMPT_RESULT_TEXT).text
        return text, text_result
