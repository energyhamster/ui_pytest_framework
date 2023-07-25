from config import BASE_URL
from pages.widgets.slider_page import SliderPage


class TestSlider:
    page_link = BASE_URL + '/slider'

    def test_slider(self, driver):
        slider_page = SliderPage(driver, self.page_link)
        slider_page.open()

        value_before, value_after = slider_page.change_slider_value()
        assert value_before != value_after, "Slider value has not been changed"


