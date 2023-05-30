from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")
    NEW_TITLE_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

    def check_opened_new_tab(self):
        self.element_is_visible(self.NEW_TAB_BUTTON).click()
        self.switch_to_tab(1)
        return self.element_is_present(self.NEW_TITLE_TEXT).text

    def check_opened_new_window(self):
        self.element_is_visible(self.NEW_WINDOW_BUTTON).click()
        self.switch_to_tab(1)
        return self.element_is_present(self.NEW_TITLE_TEXT).text
