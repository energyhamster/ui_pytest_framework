import allure

from config import BASE_URL
from pages.alerts_frames_windows.browser_windows_page import BrowserWindowsPage


class TestBrowserWindows:
    page_link = BASE_URL + '/browser-windows'

    @allure.title("Check that new tab was opened")
    def test_new_tab(self, driver):
        browser_windows_page = BrowserWindowsPage(driver, self.page_link)
        browser_windows_page.open()

        title_text = browser_windows_page.check_opened_new_tab()

        assert "This is a sample page" == title_text, "The new tab has not opened"

    @allure.title("Check that new window was opened")
    def test_new_window(self, driver):
        browser_windows_page = BrowserWindowsPage(driver, self.page_link)
        browser_windows_page.open()

        title_text = browser_windows_page.check_opened_new_window()

        assert "This is a sample page" == title_text, "The new window has not opened"
