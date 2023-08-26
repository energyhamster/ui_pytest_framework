import allure

from config import BASE_URL
from pages.widgets.tabs_page import TabsPage


class TestTabs:
    page_link = BASE_URL + '/tabs'

    @allure.title("Check that tabs was clicked")
    def test_tabs(self, driver):
        tabs_page = TabsPage(driver, self.page_link)
        tabs_page.open()

        what_tab, what_content = tabs_page.check_tabs('what_tab')
        origin_tab, origin_content = tabs_page.check_tabs('origin_tab')
        use_tab, use_content = tabs_page.check_tabs('use_tab')
        more_tab, more_content = tabs_page.check_tabs('more_tab')

        assert what_tab == 'What' and what_content != 0, "The tab 'What' was not pressed or the text is missing"
        assert origin_tab == 'Origin' and origin_content != 0, "The tab 'Origin' was not pressed or the text is missing"
        assert use_tab == 'Use' and use_content != 0, "The tab 'Use' was not pressed or the text is missing"
        assert more_tab == 'More' and more_content != 0, "The tab 'More' was not pressed or the text is missing"
