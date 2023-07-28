from config import BASE_URL
from pages.interactions.selectable_page import SelectablePage


class TestSelectable:
    page_link = BASE_URL + '/selectable'

    def test_sortable(self, driver):
        selectable_page = SelectablePage(driver, self.page_link)
        selectable_page.open()

        list_item = selectable_page.select_list_item()
        grid_item = selectable_page.select_grid_item()

        assert len(list_item) > 0, "No elements were selected"
        assert len(grid_item) > 0, "No elements were selected"
