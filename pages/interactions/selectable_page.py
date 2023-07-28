import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SelectablePage(BasePage):
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (By.CSS_SELECTOR,
                 "ul[id='verticalListContainer'] li[class='mt-2 list-group-item list-group-item-action']")
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item active list-group-item-action']")
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, "div[id='gridContainer'] li[class='list-group-item list-group-item-action']")
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, "li[class='list-group-item active list-group-item-action']")

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_item(self, tab_locator, item_locator, active_item_locator):
        self.element_is_visible(tab_locator).click()
        self.click_selectable_item(item_locator)
        active_element = self.element_is_visible(active_item_locator)
        return active_element.text

    def select_list_item(self):
        return self.select_item(self.TAB_LIST, self.LIST_ITEM, self.LIST_ITEM_ACTIVE)

    def select_grid_item(self):
        return self.select_item(self.TAB_GRID, self.GRID_ITEM, self.GRID_ITEM_ACTIVE)
