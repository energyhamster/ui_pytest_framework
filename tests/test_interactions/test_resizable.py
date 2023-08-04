from config import BASE_URL
from pages.interactions.resizable_page import ResizablePage


class TestResizable:
    page_link = BASE_URL + '/resizable'

    def test_resizable(self, driver):
        resizable_page = ResizablePage(driver, self.page_link)
        resizable_page.open()

        max_box, min_box = resizable_page.change_size_resizable_box()
        max_resize, min_resize = resizable_page.change_size_resizable()

        assert ("500px", "300px") == max_box, "Maximum size not equal to '500px', '300px'"
        assert ("150px", "150px") == min_box, "Minimum size not equal to '150px', '150px'"
        assert min_resize != max_resize, "Resizable has not been changed"
