import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TabsPage(BasePage):
    TABS_WHAT = [By.CSS_SELECTOR, "a[id='demo-tab-what']"]
    TABS_WHAT_CONTENT = [By.CSS_SELECTOR, "div[id='demo-tabpane-what']"]
    TABS_ORIGIN = [By.CSS_SELECTOR, "a[id='demo-tab-origin']"]
    TABS_ORIGIN_CONTENT = [By.CSS_SELECTOR, "div[id='demo-tabpane-origin']"]
    TABS_USE = [By.CSS_SELECTOR, "a[id='demo-tab-use']"]
    TABS_USE_CONTENT = [By.CSS_SELECTOR, "div[id='demo-tabpane-use']"]
    TABS_MORE = [By.CSS_SELECTOR, "a[id='demo-tab-more']"]
    TABS_MORE_CONTENT = [By.CSS_SELECTOR, "div[id='demo-tabpane-more']"]

    @allure.step("Check tabs")
    def check_tabs(self, name_tab):
        tabs = {
            'what_tab':
                {
                    'title': self.TABS_WHAT,
                    'content': self.TABS_WHAT_CONTENT
                },
            'origin_tab':
                {
                    'title': self.TABS_ORIGIN,
                    'content': self.TABS_ORIGIN_CONTENT
                },
            'use_tab':
                {
                    'title': self.TABS_USE,
                    'content': self.TABS_USE_CONTENT
                },
            'more_tab':
                {
                    'title': self.TABS_MORE,
                    'content': self.TABS_MORE_CONTENT
                }
        }

        tab = self.element_is_visible(tabs[name_tab]['title'])
        tab.click()
        tab_content = self.element_is_visible(tabs[name_tab]['content']).text
        return tab.text, len(tab_content)
