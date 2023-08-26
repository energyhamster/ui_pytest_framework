import allure

from config import BASE_URL
from pages.alerts_frames_windows.nested_frames_page import NestedFramesPage


class TestNestedFrames:
    page_link = BASE_URL + '/nestedframes'

    @allure.title("Check nested frames")
    def test_nested_frames(self, driver):
        nested_frames_page = NestedFramesPage(driver, self.page_link)
        nested_frames_page.open()

        parent_text, child_text = nested_frames_page.check_nested_frame()

        assert parent_text == 'Parent frame', "Nested frame does not exist"
        assert child_text == 'Child Iframe', "Nested frame does not exist"
