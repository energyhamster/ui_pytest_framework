import allure

from config import BASE_URL
from pages.alerts_frames_windows.modal_dialogs_page import ModalDialogsPage


class TestModalDialogs:
    page_link = BASE_URL + '/modal-dialogs'

    @allure.title("Check modal dialog windows")
    def test_modal_dialogs(self, driver):
        modal_dialogs_page = ModalDialogsPage(driver, self.page_link)
        modal_dialogs_page.open()

        small = modal_dialogs_page.check_small_modal_dialogs()
        large = modal_dialogs_page.check_large_modal_dialogs()

        assert small[0] == "Small Modal", "The header is not 'Small Modal'"
        assert large[0] == "Large Modal", "The header is not 'Large Modal'"
