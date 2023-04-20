from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    CHECK_BOX_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
