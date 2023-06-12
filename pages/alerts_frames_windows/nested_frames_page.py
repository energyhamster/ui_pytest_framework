from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, "p")

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.PARENT_FRAME_TEXT).text

        child_frame = self.element_is_present(self.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.CHILD_FRAME_TEXT).text

        return parent_text, child_text
