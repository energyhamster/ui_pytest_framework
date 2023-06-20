from pages.widgets.accordian_page import AccordianPage


class TestAccordian:
    page_link = 'https://demoqa.com/accordian'

    def test_accordian(self, driver):
        accordian_page = AccordianPage(driver, self.page_link)
        accordian_page.open()

        first_section_title, first_section_body = accordian_page.check_accordian("first_section")
        second_section_title, second_section_body = accordian_page.check_accordian("second_section")
        third_section_title, third_section_body = accordian_page.check_accordian("third_section")

        assert first_section_title == "What is Lorem Ipsum?" and first_section_body > 0, \
            "The header is not 'What is Lorem Ipsum?'"
        assert second_section_title == "Where does it come from?" and second_section_body > 0, \
            "The header is not 'Where does it come from?'"
        assert third_section_title == "Why do we use it?" and third_section_body > 0, \
            "The header is not 'Why do we use it?'"
