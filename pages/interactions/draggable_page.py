import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DraggablePage(BasePage):
    # Simple Tab
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-simple']")
    DRAG_ME = (By.CSS_SELECTOR, "div[id='draggableExample-tabpane-simple'] div[id='dragBox']")

    # Axis Restricted Tab
    AXIS_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-axisRestriction']")
    ONLY_X = (By.CSS_SELECTOR, "a[id='restrictedX']")
    ONLY_Y = (By.CSS_SELECTOR, "a[id='restrictedY']")

    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    def simple_drag_box(self):
        self.element_is_visible(self.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.DRAG_ME)
        before_position, after_position = self.get_before_and_after_position(drag_div)
        return before_position, after_position

    
