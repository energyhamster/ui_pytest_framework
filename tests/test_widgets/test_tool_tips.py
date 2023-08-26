import allure

from config import BASE_URL
from pages.widgets.tool_tips_page import ToolTipsPage


class TestTabs:
    page_link = BASE_URL + '/tool-tips'

    @allure.title("Check that hover over was presented")
    def test_tool_tips(self, driver):
        tool_tips_page = ToolTipsPage(driver, self.page_link)
        tool_tips_page.open()

        button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()

        assert button_text == "You hovered over the Button", "Hover over missing or incorrect content"
        assert field_text == "You hovered over the text field", "Hover over missing or incorrect content"
        assert contrary_text == "You hovered over the Contrary", "Hover over missing or incorrect content"
        assert section_text == "You hovered over the 1.10.32", "Hover over missing or incorrect content"
