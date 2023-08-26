import allure

from config import BASE_URL
from pages.elements.upload_and_download_page import UploadAndDownloadPage


@allure.feature("Upload And Download")
class TestUploadAndDownload:
    page_link = BASE_URL + '/upload-download'

    @allure.title("Check that file was uploaded")
    def test_upload_file(self, driver):
        upload_and_download_page = UploadAndDownloadPage(driver, self.page_link)
        upload_and_download_page.open()

        file_name, uploaded_file_path = upload_and_download_page.upload_file()
        assert file_name == uploaded_file_path, "The file has not been upload"

    @allure.title("Check that file was downloaded")
    def test_download_file(self, driver):
        upload_and_download_page = UploadAndDownloadPage(driver, self.page_link)
        upload_and_download_page.open()

        check_file_existing = upload_and_download_page.download_file()
        assert check_file_existing is True, "The file has not been download"
