from config import BASE_URL
from pages.widgets.progress_bar_page import ProgressBarPage


class TestProgressBar:
    page_link = BASE_URL + '/progress-bar'

    def test_slider(self, driver):
        progress_bar_page = ProgressBarPage(driver, self.page_link)
        progress_bar_page.open()

        value_before, value_after = progress_bar_page.change_progress_bar_value()
        assert value_before != value_after, "Progress Bar value has not been changed"
