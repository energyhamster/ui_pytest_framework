import allure

from config import BASE_URL
from pages.interactions.draggable_page import DraggablePage


class TestDraggable:
    page_link = BASE_URL + '/resizable'

    @allure.title("Check position of the box")
    def test_draggable(self, driver):
        draggable_page = DraggablePage(driver, self.page_link)
        draggable_page.open()

        before, after = draggable_page.simple_drag_box()

        assert before != after, "The position of the box has not been changed"

