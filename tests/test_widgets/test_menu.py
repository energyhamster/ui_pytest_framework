from pages.widgets.menu_page import MenuPage


class TestMenu:
    page_link = 'https://demoqa.com/menu'

    def test_menu(self, driver):
        menu_page = MenuPage(driver, self.page_link)
        menu_page.open()

        data = menu_page.check_menu()

        assert len(data) == 8, "Menu items do not exist or have not been selected"
