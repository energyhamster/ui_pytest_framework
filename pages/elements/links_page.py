import requests
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LinksPage(BasePage):
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, "a[id='bad-request']")

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.switch_to_tab(1)
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code, link_href

    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.BAD_REQUEST_LINK).click()
        else:
            return request.status_code
