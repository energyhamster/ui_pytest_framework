import random

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SortablePage(BasePage):
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']")
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")

    @allure.step("Get sortable item")
    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    @allure.step("Change order")
    def change_order(self, tab_locator, item_locator):
        self.element_is_visible(tab_locator).click()
        order_before = self.get_sortable_items(item_locator)
        item_list = random.sample(self.elements_are_visible(item_locator), k=2)
        self.action_drag_and_drop_to_element(item_list[0], item_list[1])
        order_after = self.get_sortable_items(item_locator)
        return order_before, order_after

    @allure.step("Change list order")
    def change_list_order(self):
        return self.change_order(self.TAB_LIST, self.LIST_ITEM)

    @allure.step("Change grid order")
    def change_grid_order(self):
        return self.change_order(self.TAB_GRID, self.GRID_ITEM)
