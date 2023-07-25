from config import BASE_URL
from pages.elements.links_page import LinksPage


class TestLinks:
    page_link = BASE_URL + '/links'

    def test_check_link(self, driver):
        links_page = LinksPage(driver, self.page_link)
        links_page.open()
        href_link, current_url = links_page.check_new_tab_simple_link()
        assert href_link == current_url, "The link is broken or url is incorrect"

    def test_broken_link(self, driver):
        links_page = LinksPage(driver, self.page_link)
        links_page.open()

        response_code = links_page.check_broken_link("https://demoqa.com/bad-request")
        assert response_code == 400, "The link is works or status code is not 400"
