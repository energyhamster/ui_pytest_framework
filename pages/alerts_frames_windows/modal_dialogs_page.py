from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ModalDialogsPage(BasePage):
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    CLOSE_SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")

    def check_small_modal_dialogs(self):
        self.element_is_visible(self.SMALL_MODAL_BUTTON).click()
        title_small_dialog = self.element_is_visible(self.TITLE_SMALL_MODAL).text
        self.element_is_visible(self.CLOSE_SMALL_MODAL_BUTTON).click()
        return title_small_dialog

    def check_large_modal_dialogs(self):
        self.element_is_visible(self.LARGE_MODAL_BUTTON).click()
        title_large_dialog = self.element_is_visible(self.TITLE_LARGE_MODAL).text
        return title_large_dialog
