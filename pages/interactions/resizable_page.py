import random

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ResizablePage(BasePage):
    RESIZABLE_BOX_HANDLE = \
        (By.CSS_SELECTOR, "div[class='constraint-area'] span[class='react-resizable-handle react-resizable-handle-se']")
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    RESIZABLE_HANDLE = \
        (By.CSS_SELECTOR, "div[id='resizable'] span[class='react-resizable-handle react-resizable-handle-se']")
    RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")

    @staticmethod
    @allure.step("Get px from width and height")
    def get_px_from_width_height(value_of_size):
        width = value_of_size.split(";")[0].split(":")[1].replace(" ", "")
        height = value_of_size.split(";")[1].split(":")[1].replace(" ", "")
        return width, height

    @allure.step("Get max and min size")
    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute("style")
        return size_value

    @allure.step("Change size of resizable box")
    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_present(self.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step("Change size resizable")
    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.RESIZABLE_HANDLE), random.randint(1, 300),
                                            random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.RESIZABLE_HANDLE), random.randint(-200, -1),
                                            random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.RESIZABLE))
        return max_size, min_size
