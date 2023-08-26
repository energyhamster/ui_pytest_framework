import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FramesPage(BasePage):
    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    TITLE_FRAME_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

    @allure.step("Check frame")
    def check_frame(self, frame_num):
        if frame_num == "frame1":
            frame = self.element_is_present(self.FIRST_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.TITLE_FRAME_TEXT).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == "frame2":
            frame = self.element_is_present(self.SECOND_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.TITLE_FRAME_TEXT).text
            self.driver.switch_to.default_content()
            return [text, width, height]
