import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MenuPage(BasePage):
    MENU_ITEM_LIST = (By.CSS_SELECTOR, "ul[id='nav'] li a")

    @allure.step("Check menu")
    def check_menu(self):
        menu_item_list = self.elements_are_present(self.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.go_to_element(item)
            data.append(item.text)
        return data
