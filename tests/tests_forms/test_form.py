from config import BASE_URL
from pages.forms.form_page import FormsPage


class TestForm:
    page_link = BASE_URL + '/automation-practice-form'

    def test_form(self, driver):
        forms_page = FormsPage(driver, self.page_link)
        forms_page.open()

        person_info = forms_page.fill_form_fields()
        result = forms_page.form_result()

        assert [person_info.first_name + " " + person_info.last_name, person_info.email] == [result[0], result[1]], \
            "The form has not been filled"
