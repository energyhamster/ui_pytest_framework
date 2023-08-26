import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from config import EXPLICIT_WAIT


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("Open URL")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Check that element is visible")
    def element_is_visible(self, locator, timeout=EXPLICIT_WAIT):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Check that elements are visible")
    def elements_are_visible(self, locator, timeout=EXPLICIT_WAIT):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Check that element is present")
    def element_is_present(self, locator, timeout=EXPLICIT_WAIT):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Check that elements are presented")
    def elements_are_present(self, locator, timeout=EXPLICIT_WAIT):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Check that element is not visible")
    def element_is_not_visible(self, locator, timeout=EXPLICIT_WAIT):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Check that element is clickable")
    def element_is_clickable(self, locator, timeout=EXPLICIT_WAIT):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Go to element")
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Action double click")
    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step("Action right click")
    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @allure.step("Switch to tab")
    def switch_to_tab(self, tab_index):
        self.driver.switch_to.window(self.driver.window_handles[tab_index])

    @allure.step("Action drag and drop by offset")
    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    @allure.step("Action drag and drop to element")
    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()
