from pages.check_box_page import CheckBoxPage


class TestCheckBox:
    def test_text_box_submit(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/text-box')
        check_box_page.open()
