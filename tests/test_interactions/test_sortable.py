import allure

from config import BASE_URL
from pages.interactions.sortable_page import SortablePage


class TestSortable:
    page_link = BASE_URL + '/sortable'

    @allure.title("Check that order of the list has changed")
    def test_sortable(self, driver):
        sortable_page = SortablePage(driver, self.page_link)
        sortable_page.open()

        list_before, list_after = sortable_page.change_list_order()
        grid_before, grid_after = sortable_page.change_grid_order()

        assert list_before != list_after, "The order of the list has not been changed"
        assert grid_before != grid_after, "The order of the grid has not been changed"
