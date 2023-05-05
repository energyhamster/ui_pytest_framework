from pages.buttons_page import ButtonsPage


class TestButtons:
    page_link = 'https://demoqa.com/buttons'

    def test_different_click_on_the_buttons(self, driver):
        buttons_page = ButtonsPage(driver, self.page_link)
        buttons_page.open()

        double = buttons_page.click_on_button("double_click")
        right = buttons_page.click_on_button("right_click")
        click = buttons_page.click_on_button("click")

        assert double == "You have done a double click", "The double click button was not pressed"
        assert right == "You have done a right click", "The right click button was not pressed"
        assert click == "You have done a dynamic click", "The dynamic click button was not pressed"


